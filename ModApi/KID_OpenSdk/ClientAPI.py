# -*- coding: utf-8 -*-
import mod.client.extraClientApi as clientApi
from SharedRes import KBaseAPI, OO_STRUCT
from GL_OPT_CLS import IBattleHandler, IUSER_RUNTIME
lambda: "By Zero123"
"""
    >> 受MOD加载先后顺序以及一些功能延后处理问题
    请勿在初始化时直接操作API 至少需要在Addon全部加载完毕后再操作

    警告: 该API文件仅用于MOD适配协作 请勿开发恶意攻击类MOD
"""

class CLIENT_GAME_SETTINGS_DEFINE:
    """ 客户端游戏设置定义 """
    GLOBAL_KID_AOPT = "GLOBAL_KID_AOPT"
    """ 全局开关 (涉及动作优化, 战斗机制, 外观形象等资源管理) """
    BATTLE_EXPANSION = "BattleExpansion"
    """ 战斗扩展 """
    CAMERA_MODE = "__CAM_MODE__"
    """ 摄像机运镜模式 """
    HURT_TEXT_RENDER = "__HURT_TEXT__"
    """ 受伤文本渲染 """
    USE_HURT_SHAKE = "__HURT_SHAKE__"
    """ 受伤震动 """
    LOCK_NATIVE_ATTACK = "__LOCK_NATIVE_ATTACK__"
    """ 锁定原生攻击 """
    USE_MOVE_ATTACK = "__USE_MOVE_ATTACK__"
    """ 启用走A模式 """
    USE_HURT_SOUND = "__USE_HURT_SOUND__"
    """ 受伤音效提示 """
    USE_BLOOM = "__USE_BLOOM__"
    """ BLOOM泛光 """
    USE_BLUR = "__USE_BLUR__"
    """ 使用屏幕模糊(运动模糊) """
    UI_ALPHA = "__UI_ALPHA__"
    """ UI透明模式 """
    HURT_EFFECT = "__HURT_EFFECT__"
    """ 受伤粒子效果 """
    USE_MASK = "__USE_MASK__"
    """ 马赛克模式(娱乐性) """

class CustomSkinEvent(OO_STRUCT):
    """ 自定义皮肤事件对象(由前置传递给CustomSkinModel绑定的变化方法) """
    # ==================== 该cls上下兼容 请勿随意修改属性表 ====================
    ERR = -1
    NOT_USE = 0
    IN_USE = 1
    def __init__(self, stateType=0):
        OO_STRUCT.__init__(self)
        self.stateType = stateType
        """ 状态类型 (0/1) 表述使用状态 -1为异常状态 未来可能加入更多状态 """

class CustomSkinModel(OO_STRUCT):
    """ 自定义皮肤模型数据类型 """
    # ==================== 该cls向上兼容 请勿随意修改属性表 ====================
    def __init__(self, skinTypeName="test", icon=None, useTexture=None, useModel=None, bindChangeCall=lambda *_: None, allowFaceExpressions=False, customAnims={}):
        # type: (str, str | None, str | None, str | None, object, bool, dict) -> None
        """
            ### CustomSkinModel 功能解读
            useModel允许使用None/steve/alex代表引用内置的动作优化模型
            当useTexture为None时引用玩家自己的皮肤数据 此外自定义SkinModel下 半透明将会自动发光同时支持Bloom
            allowFaceExpressions控制是否渲染面部表情 如果引用的是内置模型无论是否开启都将渲染面部表情

            ### 新增参数
            #### customAnims-叠加动画
            用于覆盖已有KID动画资源KEY 在取消皮肤模型后会自动恢复
        """
        OO_STRUCT.__init__(self)
        self.skinTypeName = skinTypeName
        self.icon = icon
        self.useTexture = useTexture
        self.useModel = useModel
        self._onChange = bindChangeCall
        self._customAnims = customAnims
        self.allowFaceExpressions = allowFaceExpressions
        self.loadAnims = {}
        self.loopAnim = None
        self.renderName = skinTypeName
        self._evalEventCall = None

    def setEvalEventCall(self, strEval):
        # type: (str) -> CustomSkinModel
        """ 设置事件动态执行表达式 """
        self._evalEventCall = strEval
        return self
    
    def setCustomAnims(self, newAnimsDict={}):
        """ 设置自定义动画覆盖表 """
        self._customAnims = newAnimsDict
    
    def setLoadAnimsMap(self, animDict={}):
        """ 设置加载的动画Map
            介于渲染系统实现原因 key值类型(动画/控制器)一旦确定请勿跨类型写入
            内置 kid_mod_custom_anim_con 控制器默认加载您的loopAnim资源 可重写此控制器管理其他动画/控制器
        """
        self.loadAnims = animDict
        return self
    
    def bindChangeFunc(self, func=lambda *_:None):
        """ 绑定状态改变方法 参数为: CustomSkinEvent类型 """
        self._onChange = func
        return self
    
    def setRenderName(self, name=""):
        """ 设置渲染的名称 """
        self.renderName = name
        return self
    
    def setLoopAnim(self, anim=""):
        """ 设置皮肤的循环叠加动画(通过叠加动画处理装饰品之类的表现) """
        self.loopAnim = anim
        return self
    
    def setFaceExpressionsState(self, state=True):
        """ 设置面部表情启用状态 """
        self.allowFaceExpressions = state
        return self
    
    def setIcon(self, ico=""):
        """ 设置Icon """
        self.icon = ico
        return self

    def setTexture(self, texture=""):
        """ 设置Texture """
        self.useTexture = texture
        return self

    def setModel(self, model=""):
        """ 设置Model """
        self.useModel = model
        return self

class OO_MCLS_REF:
    @staticmethod
    def bindTarget(modulePath=""):
        def _loader(cls):
            if 1 > 2:
                return cls
            module = kapi.impModFile(modulePath)
            name = cls.__name__
            return getattr(module, name)
        return _loader

    @staticmethod
    def lazyFuncBindTarget(modulePath=""):
        def _loader(func):
            funcName = func.__name__
            if 1 > 2:
                return func
            def castFunc(*args, **kwargs):
                module = kapi.impModFile(modulePath)
                return getattr(module, funcName)(*args, **kwargs)
            return castFunc
        return _loader

class _KAPI(KBaseAPI):
    def __init__(self):
        KBaseAPI.__init__(self)
        self.__ateApi = None  # type: KATE_API | None
        self.__resApi = None  # type: KRES_API | None

    def impModule(self, _path):
        # type: (str) -> object | None
        """ 导入加载模块 """
        return clientApi.ImportModule(_path)

    def getATEOpenState(self):
        # type: () -> bool
        """ 获取战斗扩展开启状态 """
        return getattr(self.getBattleExpansionAPI(), "GET_ATE_OPEN_STATE")()
    
    def setATEOpenState(self, _state = True):
        # type: (bool) -> None
        """ 设置战斗扩展开启状态 此操作不会存档(即不影响设置页信息)存档性更改请调用updateGameSettingValue """
        return getattr(self.getBattleExpansionAPI(), "SET_ATE_OPEN_STATE")(_state)

    def getGameSettingsMap(self):
        # type: () -> dict[str, int]
        """ [只读] 获取游戏设置清单 """
        return getattr(self.getBaseAPI(), "CLIENT_GET_GAME_SETTINGS_MAP")()
    
    def getGameSettingValue(self, useKey="__NONE__"):
        # type: (str) -> int
        """ 获取游戏设置状态 若不存在设置也会视为0返回(默认值) """
        return getattr(self.getBaseAPI(), "CLIENT_GET_GAME_SETTING")(useKey)

    def updateGameSettingValue(self, useKey="__NONE__", newState = 0):
        # type: (str, int) -> bool
        """ 修改游戏设置状态(存档) 该操作会立即更新资源设置 请勿频繁使用 """
        return getattr(self.getBaseAPI(), "CLIENT_SET_GAME_SETTING_VALUE")(useKey, newState)

    def regCustomFunction(self, renderText="未命名功能", funcObj=lambda: None, closeUI=True):
        # type: (str, object, bool) -> object
        """ 在更多功能中注册自定义功能(非唯一性允许多次注册)将返回此功能的object对象 可以动态取消注册 """
        return getattr(self.getBaseAPI(), "CLIENT_REG_CUSTOM_FUNCTION")(renderText, funcObj, closeUI)

    def unRegCustomFunction(self, _obj):
        # type: (object) -> None
        """ 取消注册自定义功能 """
        return getattr(self.getBaseAPI(), "CLIENT_UNREG_CUSTOM_FUNCTION")(_obj)
    
    def regCustomSkinModel(self, skinModelData):
        # type: (CustomSkinModel) -> CustomSkinModel
        """ 注册自定义皮肤模型 """
        getattr(self.getBaseAPI(), "CLIENT_REG_CUSTOM_SKIN")(skinModelData)
        return skinModelData

    def hidePlayerArmor(self, state=False):
        # type: (bool) -> None
        """ [因兼容问题暂时弃用] 设置是否隐藏本地玩家盔甲渲染(通过延迟请求低功耗自动同步服务端)
        """
        return getattr(self.getBaseAPI(), "CLIENT_HIDE_PLAYER_ARMOR")(state)

    def regItemBaseATE(self, itemName="", ateId=1):
        # type: (str, int) -> bool
        """ 注册物品默认ATE预设(对应自定义ATE中的预置逻辑id同理 0为保留值请勿使用) """
        return getattr(self.getBaseAPI(), "CLIENT_REG_ITEM_BASE_ATE")(itemName, ateId)
    
    def getATEApi(self):
        # type: () -> KATE_API
        """ 获取ATE API """
        if not self.__ateApi:
            self.__ateApi = KATE_API()
        return self.__ateApi

    def getPlayerRes(self):
        # type: () -> KRES_API
        """ 获取玩家资源管理API """
        if not self.__resApi:
            self.__resApi = KRES_API()
        return self.__resApi

    def addCustomRecmdModIN(self, icon="textures/items/diamond", titleName="Unknow MOD", text="Unknow", docText="Unknow Doc"):
        """ 在KID MOD适配/联动页面新增介绍说明 """
        return getattr(self.getBaseAPI(), "CLIENT_ADD_CUSTOM_RECMD_MODS_IN")(icon, titleName, text, docText)

    def LOAD_AOPT_TO_ENTITY_TYPE(self, entityType):
        """ 为特定生物类型加载动作优化 """
        return getattr(self.getBaseAPI(), "LOAD_AOPT_TO_ENTITY_TYPE")(entityType)

    def addOptionsPan(self, panObj):
        """ 添加自定义选项盘 """
        return getattr(self.getBaseAPI(), "CLIENT_ADD_OPTIONS_PAN")(panObj)

    def removeOptionsPan(self, panObj):
        """ 移除自定义选项盘 """
        return getattr(self.getBaseAPI(), "CLIENT_REMOVE_OPTIONS_PAN")(panObj)

    def addCustomCKLImage(self, img="textures/models/xxx"):
        """ 添加自定义刀光选项纹理图 文件所在路径必须在textures/models/* """
        return getattr(self.getBaseAPI(), "CLIENT_ADD_CUSTOM_CKL_IMGS")([img])

    def batchAddCustomCKLImgs(self, imgs=["textures/models/xxx"]):
        """ 批量添加自定义刀光选项纹理图 文件所在路径必须在textures/models/* """
        return getattr(self.getBaseAPI(), "CLIENT_ADD_CUSTOM_CKL_IMGS")(imgs)

    def call(self, funcName="", *args, **kwargs):
        """ 标准化调用服务端注册函数(通过延迟数据包) """
        return getattr(self.getBaseAPI(), "STD_CLIENT_CALL")(funcName, args, kwargs)

class KATE_API(_KAPI):
    def getATEApi(self):
        return None
    
    def getAttackState(self, mustStop=False):
        # type: (bool) -> bool
        """ 获取ATE是否处于攻击状态
            @mustStop 该值为False时后摇阶段也视为非攻击状态
        """
        return getattr(self.getBattleExpansionAPI(), "GET_ATE_ATTACKING_STATE")(mustStop)

    def breakAttack(self, force=False):
        # type: (bool) -> bool
        """ 打断ATE攻击状态
            @force 当该值为False时仅打断处于非后摇阶段的攻击逻辑 可以满足大多数动画过渡流畅度表现 设置为True时处于后摇的攻击逻辑也会打断
        """
        return getattr(self.getBattleExpansionAPI(), "BREAK_ATE_ATTACK")(force)

    def getRollState(self):
        # type: () -> bool
        """ 获取是否处于ATE翻滚状态 """
        return getattr(self.getBattleExpansionAPI(), "GET_ATE_ROLL_STATE")()
    
    def getDefenseState(self):
        # type: () -> bool
        """ 获取ATE是否处于防御状态 """
        return getattr(self.getBattleExpansionAPI(), "GET_ATE_DEFENSE_STATE")()
    
    def breakDefense(self):
        # type: () -> bool
        """ 打断防御状态 """
        return getattr(self.getBattleExpansionAPI(), "BREAK_ATE_DEFENSE")()
    
    def getChargingState(self):
        # type: () -> bool
        """ 获取是否处于蓄力状态 """
        return getattr(self.getBattleExpansionAPI(), "GET_ATE_CHARGING_STATE")()

    def breakCharging(self):
        # type: () -> bool
        """ 打断蓄力状态 """
        return getattr(self.getBattleExpansionAPI(), "BREAK_ATE_CHARGING")()

    def getAnyState(self, attMustStop=False):
        # type: (bool) -> bool
        """ 获取是否处于任意状态
            @attMustStop 对应getAttackState的条件参数
        """
        return getattr(self.getBattleExpansionAPI(), "GET_ATE_ANY_STATE")(attMustStop)
    
    def setAttackRangeOffset(self, v=0.0):
        # type: (float | int) -> None
        """ 设置ATE攻击范围偏移(原范围基础上追加) 全局独立层区 """
        return getattr(self.getBattleExpansionAPI(), "SET_ATE_MODATT_RANGE_OFFSET")(v)

    def setItemRangeOffset(self, itemName="", v=0.0):
        # type: (str, float | int) -> None
        """ 设置特定物品ATE攻击范围偏移(原范围基础上追加) 个体独立层区 """
        return getattr(self.getBattleExpansionAPI(), "SET_ATE_ITEM_RANGE_OFFSET")(itemName, v)

    def setDisATEState(self, state=True):
        # type: (bool) -> None
        """ 设置是否禁用ATE操作(自动打断) 禁用后UI按键将处于不可交互状态适用于技能扩展
            PS: 打断逻辑不支持翻滚 请在判定为非翻滚状态下扩展自己的技能逻辑
        """
        return getattr(self.getBattleExpansionAPI(), "DIS_ATE_STATE")(state)
    
    def getCanOverlayOperation(self):
        # type: () -> bool
        """ 获取是否允许叠加ATE操作(自定义技能类扩展)
            该方法将会自动判断 翻滚状态/其他互斥操作情况如setDisATEState 确保始终只能进行一种操作
            通常搭配setDisATEState, setDisKIDAnimState一起使用 在技能能力播放完毕后应恢复禁用状态
        """
        return bool(getattr(self.getBattleExpansionAPI(), "GET_CAN_OVERLAY_ATE_OPERATION")())
    
    def regItemDefaultATEId(self, itemName="", ateId=1):
        # type: (str, int) -> None
        """ 注册物品基础ATE_ID(对应游戏编辑面板序号) """
        return getattr(self.getBattleExpansionAPI(), "REG_ITEM_DEFAULT_ATE_ID")(itemName, ateId)

    def regCustomQuickStrikeButton(self, ueryId=5000, renderText="自定义切手", docRender=""):
        # type: (int, str, str) -> object
        """ 注册自定义切手技选项(返回tab文本句柄 可以动态修改) """
        return getattr(self.getBattleExpansionAPI(), "ADD_CUSTOM_QUICK_STRIKE_BUTTON")(ueryId, renderText, docRender)

    def regCustomQuickStrike(self, regQuickId=5000, regObj=None):
        """ 注册自定义切手技WITH ID """
        return getattr(self.getBattleExpansionAPI(), "REG_CUSTOM_QUICK_FUNC_WITH_ID")(regQuickId, regObj)

    def regItemUseCustomQuickStrike(self, itemList=[], obj=None):
        """ 注册自定义切手技到特定物品(itemList允许批量注册多个物品) """
        return getattr(self.getBattleExpansionAPI(), "REG_CUSTOM_QUICK_FUNC_WITH_ITEMS")(itemList, obj)

    def GET_ATE_USER_RUNTIME(self):
        # type: () -> type[IUSER_RUNTIME]
        """ 获取用户运行时数据 可以管理ATE UI相应事件 """
        return getattr(self.getBattleExpansionAPI(), "GET_ATE_USER_RUNTIME")()

    def getBattleHandlerCls(self):
        # type: () -> type[IBattleHandler]
        """ 获取BattleHandler类 """
        return getattr(self.getBattleExpansionAPI(), "GET_ATE_BATTLE_HANDLER_CLS")()
    
    def regCustomJsonATE(self, joDict):
        # type: (dict) -> None
        """ 注册JSON ATE扩展 注意:静态资源的合批处理是在AddonFinish事件下进行的 请在此之前调用 亦或者将监听事件优先级提高(内部使用0) """
        return getattr(self.getBattleExpansionAPI(), "JSON_CLIENT_REG_CUSTOM_ATE")(joDict)

    def getRuntimeATECustomId(self):
        # type: () -> str
        """ 获取 当前运行的ATE自定义ID 若为内置ATE/非运行状态则返回空字符串 """
        return getattr(self.getBattleExpansionAPI(), "GET_RUN_ATE_CUSTOM_ID")()

class KRES_API(_KAPI):
    def getPlayerRes(self):
        return None
    
    def setQuery(self, queryName="", value=0.0):
        # type: (str, float) -> None
        """ 通过延迟同步队列设置玩家query(全局同步) """
        return getattr(self.getBaseAPI(), "CLIENT_SET_PLAYER_QUERY")(queryName, value)
    
    def setDisKIDAnimState(self, state=True):
        # type: (bool) -> None
        """ [延迟同步|请勿频繁调用] 设置是否禁用动作优化(线性打断) 此时会过渡回到无动画状态以便叠加其他技能动画 """
        return getattr(self.getBaseAPI(), "CLIENT_SET_BLOCK_ANIMATION")(state)

    def regClientPlayerStaticRes(self, resDict={}):
        # type: (dict) -> None
        """ 注册客户端玩家静态资源(类JSON格式) 注意:静态资源的合批处理是在AddonFinish事件下进行的 请在此之前调用 亦或者将监听事件优先级提高(内部使用0) """
        return getattr(self.getBaseAPI(), "REG_CLIENT_PLAYER_STATIC_RES")(resDict)

@OO_MCLS_REF.lazyFuncBindTarget("GL_API")
def STATIC_LOCAL_PLAYER_EFFECT_LISTENER(queryBindName):
    """ 装饰器静态注册玩家效果监听器 """
    def _loader(func):
        return func
    return _loader

@OO_MCLS_REF.lazyFuncBindTarget("GL_API")
def STATIC_LOCAL_MOB_EFFECT_LISTENER(queryBindName):
    """ 装饰器静态注册全生物效果监听器 """
    def _loader(func):
        return func
    return _loader

KAPI = kapi = _KAPI()
