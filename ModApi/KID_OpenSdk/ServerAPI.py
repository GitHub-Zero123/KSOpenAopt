# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi
from SharedRes import KBaseAPI, OO_MethodForward
from GL_OPT_CLS import JSONRenderData, GL_RES
lambda: "By Zero123"
"""
    >> 受MOD加载先后顺序以及一些功能延后处理问题
    请勿在初始化时直接操作API 至少需要在Addon全部加载完毕后再操作

    警告: 该API文件仅用于MOD适配协作 请勿开发恶意攻击类MOD
"""

SHARED_MEMORY_KEY = "KID_SHARED_MEMORY"
""" KID共享内存块 """

class _SharedMemory:
    """ 共享内存管理 """
    def __init__(self, bindKey=SHARED_MEMORY_KEY):
        self._bindKey = bindKey
        self.mcSystem = serverApi.GetSystem("Minecraft","game")

    def getMemoryMap(self):
        # type: () -> dict[str, object]
        """ 获取内存视图 """
        bindKey = self._bindKey
        if not hasattr(self.mcSystem, bindKey):
            setattr(self.mcSystem, bindKey, dict())
        return getattr(self.mcSystem, bindKey)

    def getValue(self, keyName, defaultValue=None):
        # type: (str, object | None) -> object
        return self.getMemoryMap().get(keyName, defaultValue)

class KSharedMemory(_SharedMemory):
    def __init__(self):
        _SharedMemory.__init__(self)

    def getHandlesView(self, typeName=""):
        # type: (str) -> list[KResHandle]
        dic = self.getMemoryMap()
        key = "{}_Handles".format(typeName)
        if not key in dic:
            dic[key] = list()
        return dic[key]

    def callResHandles(self, typeName="", playerId="", key="", value="", tempData={}):
        # type: (str, str, str, str, dict) -> None
        dataList = self.getHandlesView(typeName)
        for handle in dataList:
            try:
                value = handle.resCheck(playerId, key, value, tempData) or value
            except Exception:
                import traceback
                traceback.print_exc()
        for handle in dataList[::]:
            try:
                handle.update(playerId, key, value)
            except Exception:
                import traceback
                traceback.print_exc()

    def setPlayerModel(self, playerId, keyName, value, tempData={}):
        # type: (str, str, str, dict) -> None
        return self.callResHandles("model", playerId, keyName, value, tempData)

    def setPlayerAnim(self, playerId, keyName, value, tempData={}):
        # type: (str, str, str, dict) -> None
        return self.callResHandles("anims", playerId, keyName, value, tempData)

    def getPlayerModelHandlesView(self):
        # type: () -> list[KResHandle]
        return self.getHandlesView("model")

    def getPlayerAnimHandlesView(self):
        # type: () -> list[KResHandle]
        return self.getHandlesView("anims")

class KResHandle:
    def resCheck(self, playerId, resKey, resData, argsDict):
        # 校验资源数据 返回的数据将传递给下一个Handle对象 直到最终结束 选中唯一的结果调用update
        pass

    def update(self, playerId, resKey, resData):
        pass

class _KAPI(KBaseAPI):
    def __init__(self):
        KBaseAPI.__init__(self)
        self.__ateApi = None  # type: KATE_API | None
        self._sharedMemory = None   # type: KSharedMemory | None

    def getSharedMemory(self):
        """ [未启用] 获取动作优化相关共享管理内存 """
        if not self._sharedMemory:
            self._sharedMemory = KSharedMemory()
        return self._sharedMemory

    def getATEApi(self):
        # type: () -> KATE_API
        """ 获取ATE API """
        if not self.__ateApi:
            self.__ateApi = KATE_API()
        return self.__ateApi

    def impModule(self, _path):
        # type: (str) -> object | None
        """ 导入加载模块 """
        return serverApi.ImportModule(_path)

    def setATEItemHurt(self, itemName="", value=4):
        """ 主动注册ATE物品伤害数值 (非注册物品将采用内置的算法计算伤害) """
        return getattr(self.getBattleExpansionAPI(), "SET_ATE_ITEM_HURT")(itemName, value)
    
    def hidePlayerArmor(self, playerId, state=False):
        # type: (str, bool) -> None
        """ [因兼容问题暂时弃用] 服务端隐藏玩家盔甲 """
        return getattr(self.getBaseAPI(), "SERVER_HIDE_PLAYER_ARMOR")(playerId, state)
    
    def getPlayerRes(self, playerId):
        # type: (str) -> KRES_API
        """ 获取玩家资源API """
        return KRES_API(playerId)

class KATE_API(_KAPI):
    def getATEApi(self):
        return None

    def regRPCQuickStrikeComp(self, rpcCompName="", rpcCompCls=type):
        """ 注册RPC切手技组件 用于绑定关联调用 """
        return getattr(self.getBattleExpansionAPI(), "REG_RPC_QUICK_STRIKE_COMP_CLS")(rpcCompName, rpcCompCls)

class KRES_API(_KAPI):
    def __init__(self, playerId=""):
        _KAPI.__init__(self)
        self.playerId = playerId
        self._resPtr = None     # type: object | None
        """ 引用动作优化内原始玩家资源对象的指针 """
        self.forwardTool = None # type: OO_MethodForward | None
        """ 方法转发器 """
        self._initResPtr()

    def _initResPtr(self):
        # type: () -> object
        """ 初始化资源操作指针 """
        if not self._resPtr:
            # 初始化并绑定转发方法 (直接调用原始对象中的方法而不是静态模型的)
            self._resPtr = getattr(self.getBaseAPI(), "SERVER_GET_PLAYER_RES")(self.playerId)
            self.forwardTool = forwardTool = OO_MethodForward(self, self._resPtr)
            forwardTool.bindMethod(self.addOptPass)
            forwardTool.bindMethod(self.setQuery)
            forwardTool.bindMethod(self.setQueryNow)
            forwardTool.bindMethod(self.getQuery)
            forwardTool.bindMethod(self.loadJSONRenderData)
            forwardTool.bindMethod(self.releaseJSONRenderData)
        return self._resPtr

    def setDisKIDAnimState(self, state=True):
        # type: (bool) -> None
        """ 设置是否禁用动作优化(线性打断) 此时会过渡回到无动画状态以便叠加其他技能动画 """
        return getattr(self.getBaseAPI(), "SERVER_SET_BLOCK_ANIMATION")(self.playerId, state)
    
    def restOptAnim(self, animKey):
        # type: (str) -> bool
        """ 尝试重置特定的Anims Key(恢复到KID动作优化默认动画) """
        return getattr(self.getBaseAPI(), "SERVER_PLAYER_REST_OPT_ANIM")(self.playerId, animKey)

    def addOptPass(self, optObj):
        # type: (GL_RES) -> None
        """ 添加资源通道操作 """
        return None
    
    def setQuery(self, queryName="", value=0.0):
        # type: (str, float) -> None
        """ 设置节点 延迟汇总计算更新 """
        return None

    def setQueryNow(self, queryName="", value=0.0):
        # type: (str, float) -> None
        """ 设置节点并立即汇总更新 """
        return None

    def getQuery(self, queryName=""):
        # type: (str) -> float | None
        """ 获取节点 """
        return 0.0
    
    def loadJSONRenderData(self, data, SCRIPT_ANIMATE_AUTO_REPLACE = False):
        # type: (JSONRenderData, bool) -> None
        """ 加载JSON渲染对象 """
        return None
    
    def releaseJSONRenderData(self, data, fixDefaultRes = True, emptyAnim = None, emptyAnimCon = None):
        # type: (JSONRenderData, bool, str | None, str | None) -> None
        """ 释放JSON渲染对象 """
        return None

KAPI = kapi = _KAPI()