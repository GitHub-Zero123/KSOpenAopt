# -*- coding: utf-8 -*-
from STATE_MODEL import (
    MODEL_HistoricalOptManager,
    MODEL_AdvancedATEStateManager,
    MODEL_PlayerVitalityManager,
    MODEL_PlayerEnergyManager,
    MODEL_QuickStrikeManager,
    MODEL_AdvancedATEState
)

class MODEL_BASECONFIG:
    delayRecoveryMoveTime = 0.2
    restTime = 999.0

class MODEL_NewDamageData:
    def __init__(self, _damageMut = 1, _damageRange = 3.0, _damageType = 0, _breakBlockEffect = False):
        pass

class MODEL_AttackData:
    def __init__(self, 
        attackTime = 2.08,
        hittingTime = 0.2,
        breakTime = 0.35,
        damageMut = 1,
        damageRange = 3.0,
        damageType = 0,
        moveMut = 0.2,
        delayRecoveryMoveTime = MODEL_BASECONFIG.delayRecoveryMoveTime,
        restTime = MODEL_BASECONFIG.restTime,
        extDamageTimeLine = {},
        hitVec = (0.0, 0.0, 0.0),
        useBoneTracking = False,
        extraPhysicalExertion = 0.0,
        breakBlockEffect=False,
        bindCustomFunc = None,
        bindEventHandler=None,
        breakTimeMove=None,
        forceUseOffHandCalculation=False,
    ):
        pass

class MODEL_SkillAttackPreset:
    def __init__(self, attackData, disJumpBreak=True, useOffHand=False, bindAttackHSValue=None, bindQuery="", subValueId=-1145):
        # type: (MODEL_AttackData, bool, bool, bool, str, int) -> None
        pass

class MODEL_AttackPreset:
    pass

class MODEL_OnceAttackPreset(MODEL_AttackPreset):
    pass

class MODEL_ChargeUpAttackData:
    def __init__(self, maxTime = 2.0, attackData = MODEL_AttackData(), segmentedCharging = {}, minChargeMutTime=None):
        # type: (float, MODEL_AttackData, dict[str, MODEL_AttackData], float) -> None
        self.maxTime = maxTime
        self.attackData = attackData
        self.segmentedCharging = segmentedCharging
        self.segmentedChargingList = [] # type: list[tuple[float, MODEL_AttackData]]
        self.minChargeMutTime = minChargeMutTime
        self._lastIndex = 0
    
    def getMinMut(self):
        """ 获取需要最小多少蓄力比率才能发起攻击 """
        return 0.0

    def _initSegmentedChargingMap(self):
        # type: (float) -> list[MODEL_AttackData]
        pass
    
    def matchAttackData(self, timeMut=1.0):
        # type: (float) -> MODEL_AttackData
        """ 从比率时间线匹配AttackData """
        pass

    def matchAttackDataIndex(self, timeMut=1.0):
        # type: (float) -> int
        """ 基于比率时间匹配蓄力下标 """
        pass
    
    def updateWithTimeMut(self, timeMut=1.0, onceAttackPreset=None):
        # type: (float, MODEL_OnceAttackPreset) -> int
        """ 基于时间参数更新attackData """
        pass

class MODEL_BattleExpansionConfig:
    enableState = False
    """ 启用状态 """
    defaultPreCls = None    # type: type[MODEL_AttackPreset] | None
    """ 默认预设类 """
    presetObj = None        # type: MODEL_AttackPreset | None
    """ 当前预设对象 """
    itemTypeMap = {}        # type: dict[str, type[MODEL_AttackPreset]]
    """ 基于物品类型注册的预设 """
    itemNameMap = {}        # type: dict[str, type[MODEL_AttackPreset]]
    """ 基于物品名称注册的预设 """
    customATEMap = {}       # type: dict[int, type[MODEL_AttackPreset]]
    """ 内置自定义ATE Map """
    customOffATEMap = {}    # type: dict[int, type[MODEL_AttackPreset]]
    """ 内置自定义副手ATE """
    lastItemName = None     # type: str | None
    """ 储存记录上一个物品名称 """
    needUpdate = False
    _initUI = False
    """ UI是否初始化完毕 """
    _lastRollTime = 0
    _lastRollAttackTime = 0
    _rollTime = 0.5
    _rollAttackTime = 0.85
    """ 翻滚后连招的持续时间 """
    _isRolling = False
    _breakRollHandler = lambda: None
    battleTimerSet = set()
    modAttRangeOf = 0
    modItemAttRangeOf = {}  # type: dict[str, int | float]
    disGlobalUIOpt = False
    """ 禁用全局操作 """
    offHandColorMode = 0
    """ 副手色彩模式 """
    advancedStateManager = MODEL_AdvancedATEStateManager()
    """ 高级状态管理器 """
    playerVitalityManager = MODEL_PlayerVitalityManager()
    """ 玩家体力管理器 """
    historicalOptManager = MODEL_HistoricalOptManager()
    """ 记录历史操作的管理器 """
    playerEnergyManager = MODEL_PlayerEnergyManager(0, 100, 0, 45)
    """ 玩家气势管理器 """
    quickStrikeManager = MODEL_QuickStrikeManager()
    """ 切手技管理器 """

    class ROLL_DATA:
        _LAST_MODE_ID = 0
        _LAST_MOVE_VEC = None

    class ATE_MANAGER:
        @staticmethod
        def getATEIndex():
            # type: () -> int
            """ 获取当前ATE的攻击下标(如果未攻击则返回-1) """
            pass

        @staticmethod
        def getATESafeBreakState(minTime=None):
            # type: (float | None) -> bool
            """ 获取当前ATE对象是否可以被安全的打断切入 """
            pass

        @staticmethod
        def getIsAttackATE():
            """ 获取当前ATE对象是不是战斗类的(非default的) """
            pass

        @staticmethod
        def getIsInAttackRecoveryInterval():
            """ 检查是不是处于攻击后摇区间 """
            return False

        @staticmethod
        def getSwordSlippedState():
            """ 获取收刀状态 """
            return False

        @staticmethod
        def getChargeIndex():
            # type: () -> int
            """ 获取蓄力Index 如果存在否则返回-1 """
            pass

        @staticmethod
        def getChargeBit():
            # type: () -> float
            """ 获取蓄力攻击持续比例 """
            pass

        @staticmethod
        def setHurtSound(newSound="", volume=1):
            # type: (str, int) -> None
            """ 设置命中的受伤音效 """
            pass

        @staticmethod
        def getWorkingIndex():
            # type: () -> int
            """ 获取当前持续的index """
            pass

        @staticmethod
        def setOnceWorkingStartIndex(nextIndex=0, wTime=3.2):
            """ 尝试设置一次下一次开始的初始index """
            pass

        @staticmethod
        def clearOnceWorkingStartIndex():
            pass
        
        @staticmethod
        def setOnceBRKRestStartIndex(wTime=3.2):
            """ 设置一次默认重置恢复Index """
            pass

    @staticmethod
    def modSelfDisGlobalUIOpt():
        # type: () -> bool
        """ mod自我禁止操作状态 """
        pass

    @staticmethod
    def userEventCall(eventName=""):
        pass

    @staticmethod
    def breakAllDefaultOpt():
        """ 打断所有默认操作(不包括翻滚) """
        pass

    @staticmethod
    def deepBreakAllOpt():
        """ 深度打断所有操作(包括翻滚) """
        pass

    @staticmethod
    def getAdvancedStatus():
        # type: () -> bool
        """ 获取是否处于高级状态下 如僵硬值 """
        pass

    @staticmethod
    def addAdvancedState(obj):
        # type: (MODEL_AdvancedATEState) -> bool
        """ 加载高级状态(优先级大于常规攻击逻辑) 翻滚是个例外如果处于翻滚中一切操作都无法触发 除非显性调用打断 """
        pass

    @staticmethod
    def isRolling():
        # type: () -> bool
        """ 获取是否处于翻滚状态 """
        pass

    @staticmethod
    def breakDefaultRoll():
        pass

    @staticmethod
    def setRoll(useEvading=True):
        """ 设尝试置翻滚 """
        pass

    @staticmethod
    def useRollBackState():
        """ 使用翻滚后置状态 如果成功将会消除 """
        pass