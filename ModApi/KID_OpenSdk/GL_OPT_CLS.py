# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi
from SharedRes import OO_CLSForward, UNIVERSAL_STRUCT
lambda: "By Zero123 仅适用于服务端"

def _IMP_MODULE(modulePath):
    # type: (str) -> object
    return serverApi.ImportModule("KidUltra.{}".format(modulePath))

def _IMP_GLR_RES_MODULE():
    # type: () -> object
    return _IMP_MODULE("QuModLibs.Include.GL_Render.SharedRes")

def _GET_GLR_RES_CLS(clsName=str()):
    # type: (str) -> type
    try:
        _module = _IMP_GLR_RES_MODULE()
        if not "." in clsName:
            return getattr(_module, clsName)
        parent = _module
        for name in clsName.split("."):
            parent = getattr(parent, name)
        return parent
    except:
        pass
    return UNIVERSAL_STRUCT

class JSONRenderData(OO_CLSForward):
    """ JSON渲染参数 """
    # ======== 一些常用的材料定义 ========
    ENTITY = "entity"
    ENTITY_ALPHATEST = "entity_alphatest"
    ENTITY_EMISSIVE_ALPHA = "entity_emissive_alpha"
    ENTITY_EMISSIVE ="entity_emissive"

    def __init__(self,
            materials = {}, textures = {},
            geometry = {}, animate = [],
            animations = {}, render_controllers = [],
            particle_effects = {}, sound_effects = {}
        ):
        OO_CLSForward.__init__(self)
        self.setBindPtr(
            _GET_GLR_RES_CLS("JSONRenderData")(
                materials = materials,
                textures = textures,
                geometry = geometry,
                animate = animate,
                animations = animations,
                render_controllers = render_controllers,
                particle_effects = particle_effects,
                sound_effects = sound_effects,
            )
        )

class GL_RES(OO_CLSForward):
    """ GL资源操作类型 """
    def __init__(self, *args, **kwargs):
        OO_CLSForward.__init__(self)
        self.setBindPtr(
            _GET_GLR_RES_CLS("GL_RES_OPT.{}".format(self.__class__.__name__))(
                *args, **kwargs
            )
        )

class GL_TEXTURE(GL_RES):
    """ 纹理资源 """
    def __init__(self, key, value):
        GL_RES.__init__(self, key, value)

class GL_GEOMETRY(GL_RES):
    """ 模型资源 """
    def __init__(self, key, value):
        GL_RES.__init__(self, key, value)

class GL_MATERIAL(GL_RES):
    """ 材质资源 """
    def __init__(self, key, value):
        GL_RES.__init__(self, key, value)

class GL_ANIM(GL_RES):
    """ 动画/控制器资源 """
    def __init__(self, key, value):
        GL_RES.__init__(self, key, value)

class GL_PARTICLE_EFFECT(GL_RES):
    """ 粒子资源 """
    def __init__(self, key, value):
        GL_RES.__init__(self, key, value)

class GL_RENDER_CONTROLLER(GL_RES):
    """ 渲染控制器资源 """
    def __init__(self, key, value):
        GL_RES.__init__(self, key, value)

class GL_SCRIPT_ANIMATE(GL_RES):
    """ ANIMATE节点资源 """
    def __init__(self, key, value, autoReplace = False):
        GL_RES.__init__(self, key, value, autoReplace = autoReplace)
        
class GL_SOUND_EFFECT(GL_RES):
    """ 音效资源 """
    def __init__(self, key, value):
        GL_RES.__init__(self, key, value)

class GL_PLAYER_SKIN(GL_RES):
    """ 玩家皮肤纹理资源 """
    def __init__(self, value):
        GL_RES.__init__(self, value)

class OPTIONS_PAN:
    """ 选项盘对象 描述了其持有一系列选民 """
    # 截至当前版本 单个选项盘至多渲染8个元素 但超过限制也是允许的
    class OPTIONS_NODE:
        """ 选项盘节点 """
        def __init__(self, renderText="", bindClick=lambda: None):
            self._version = 1   # 数据类型版本
            self.renderText = renderText
            self.bindClick = bindClick

        def getText(self):
            # 文本获取 每Tick刷新
            return self.renderText

        def onClick(self):
            self.bindClick()
            return True
        
        def getDocs(self):
            # 获取doc描述
            return None

    _NULL_NODE = OPTIONS_NODE()
    # 优先级参考规范
    HAND_ITEM_PRIORITY = 50
    GLOBAL_ATE_PRIORITY = 75
    GLOBAL_DEFAULT_PRIORITY = 100

    def __init__(self, renderTitle="", childList=[], priority=100):
        # type: (str, list[OPTIONS_PAN.OPTIONS_NODE], int | float) -> None
        self._version = 1   # 数据类型版本
        self.renderTitle = renderTitle
        self.priority = priority
        self.childList = childList

    def getTitle(self):
        # 标题数据返回 Tick刷新
        return self.renderTitle

    def getChilds(self):
        # CHILDS更新 Tick刷新
        return self.childList

    def getPriority(self):
        # 优先级数据返回 越小越靠前 单次更新
        return self.priority

class IBattleHandler:
    def __init__(self, args):
        # type: (dict) -> None
        self._contextArgs = args or {}
        self._loadState = False
        self._safeLoadState = False

    def needBreak(self):
        return True
    
    def safeCheck(self):
        return False

    def _onLoad(self):
        pass

    def _onUnLoad(self):
        pass

    def onLoad(self):
        pass

    def onUnLoad(self):
        pass

class IUSER_RUNTIME:
    clickButtonFinders = []         # type: list[function]
    """ 单点攻击按钮 """
    longClickButtonFinders = []     # type: list[function]
    """ 长按攻击按钮 """
    rollButtonFinders = []          # type: list[function]
    """ 翻滚按钮 """
    defenseButtonFinders = []       # type: list[function]
    """ 防御按钮 """

    @staticmethod
    def addDisQuickButtonRef():
        """ 添加切手技禁用引用 """
        pass

    @staticmethod
    def removeDisQuickButtonRef():
        """ 移除一次切手技禁用引用 """
        pass