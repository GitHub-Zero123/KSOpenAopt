# -*- coding: utf-8 -*-
lambda: "By Zero123"

Unknown = type("Unknown",(object,),{})  # 有时候 这比None管用

class OO_STRUCT(object):
    # 针对面向对象的上下兼容实现 当旧版对象不包含特定属性时访问并不会抛出异常而是以None代替
    def __init__(self):
        self._contextIN = {}
        
    def _getData(self):
        return {k:getattr(self, k) for k in dir(self) if not k.startswith("__")}
    
    def __getattribute__(self, name):
        # type: (str) -> object | None
        try:
            return object.__getattribute__(self, name)
        except:
            pass
        return None

class OO_UniversalStruct(object):
    def __init__(self):
        pass

    def __getattribute__(self, __name):
        return self

    def __call__(self, *args, **kwargs):
        return self

NULL_STRUCT = OO_STRUCT()
UNIVERSAL_STRUCT = OO_UniversalStruct()

class OO_MethodForward:
    # 针对面向对象实现的方法转发(兼容实现)
    def __init__(self, fromObject, targetPtr):
        # type: (object, object) -> None
        self.fromObject = fromObject
        self.targetPtr = targetPtr
    
    def bindMethod(self, methodObj):
        # type: (object) -> None
        """ 绑定转发方法 """
        methodName = methodObj.__name__
        if not hasattr(self.targetPtr, methodName):
            print("目标方法绑定失败 {}".format(methodName))
            return
        setattr(self.fromObject, methodName, getattr(self.targetPtr, methodName))

class OO_CLSForward(object):
    # 针对面向对象实现的class转发
    def __init__(self):
        self._BIND_PTR = None

    def setBindPtr(self, ptr):
        # type: (object) -> OO_CLSForward
        self._BIND_PTR = ptr
        return self
    
    def __getattribute__(self, name):
        # type: (str) -> object
        if name in ("__init__", "setBindPtr", "_BIND_PTR", "__class__"):
            return object.__getattribute__(self, name)
        if not self._BIND_PTR:
            raise Exception("无效的绑定地址")
        return getattr(self._BIND_PTR, name)

class KBaseAPI:
    def __init__(self):
        self.modDirName = "KidUltra"
        self.cacheMap = {}
    
    def cout(self, _text):
        print("[{}] {}".format(self.__class__.__name__, _text))

    def impModule(self, _path):
        # type: (str) -> object | None
        return Unknown
    
    def impModFile(self, filePath):
        # type: (str) -> object | None
        if filePath in self.cacheMap:
            return self.cacheMap[filePath]
        data = self.impModule("{}.{}".format(self.modDirName, filePath))
        self.cacheMap[filePath] = data
        return data

    def getBattleExpansionAPI(self):
        return self.impModFile("BattleExpansion.API")

    def getBaseAPI(self):
        return self.impModFile("GL_API")

    def hasMod(self):
        # type: () -> bool
        """ 获取KID动作优化是否已经加载 """
        if self.impModFile("__init__"):
            return True
        return False

    def _hasMod(self):
        state = self.hasMod()
        if not state:
            self.cout("未找到KID动作优化")
        return state

    def getStaticPlayerRes(self):
        # type: () -> dict
        """ 获取动作优化配置中的静态玩家资源 """
        if not self._hasMod():
            return {}
        return getattr(self.impModFile("PlayerRes"), "PlayerRes")

    def getStaticCustomQuery(self):
        # type: () -> list
        """ 获取动作优化配置中的静态自定义节点 """
        if not self._hasMod():
            return []
        return getattr(self.impModFile("QuModLibs.Include.CT_Render.Configure"), "QueryList")
