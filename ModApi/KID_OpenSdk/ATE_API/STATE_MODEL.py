# -*- coding: utf-8 -*-
lambda: "该模块提供了切手技/其他状态相关的结构模型以便补全库支持"

class MODEL_UserOPTEvent:
    def onUserClickAttackButton(self):
        """ 状态期间用户点击攻击按钮触发 """
        pass

    def onUserTryChangeAttack(self):
        """ 状态期间用户尝试长按蓄力攻击键 """
        pass

    def onUserTryFreeChangeAttack(self):
        """ 状态期间用户尝试释放长按蓄力攻击键 """
        pass

    def onUserTryRoll(self):
        """ 状态期间用户尝试点击翻滚键位 """
        pass

    def onUserTryDefense(self):
        """ 状态期间用户尝试防御触发 """
        pass

    def onUserTryFreeDefense(self):
        """ 状态期间用户释放尝试防御触发 """
        pass

    def onPlayerHurtOther(self):
        """ 玩家命中目标时触发 """
        pass

    def onATEChange(self):
        """ 玩家改变ATE类型后触发 """
        pass

class MODEL_AdvancedATEState(MODEL_UserOPTEvent):
    """ 基本状态 """
    def __init__(self):
        self._quickTouch = False
        self._isLongTouch = False
        self.hitTargetCount = 0
        self._CACHE_PLAYER_IMMUNE_DAMAGE = None

    @classmethod
    def CLS_LOAD_STATE(cls, *args, **kwargs):
        pass

    @classmethod
    def CLS_REMOVE_STATE(cls):
        pass

    @classmethod
    def CLS_IS_STATE_WORKING(cls):
        pass

    def CACHE_PLAYER_IMMUNE_DAMAGE(self, state=True):
        pass
    
    def SERVER_SET_MOVE_VEC(self, absVec=0.5):
        """ 发包到服务端设置移动向量 """
        pass

    def PLAYER_IMMUNE_DAMAGE(self, state=True, useCache=False):
        pass
    
    def onUserTryChangeAttack(self):
        """ 状态期间用户尝试长按蓄力攻击键 """
        pass

    def onUserTryFreeChangeAttack(self):
        """ 状态期间用户尝试释放长按蓄力攻击键 """
        pass

    def onUserLongTouchQuickStrike(self):
        """ 状态期间用户长按切手技 """
        pass
    
    def onUserTryFreeQuickStrike(self):
        """ 状态期间用户尝试松手切手技 """
        pass

    def getPriority(self):
        return 10

    def onPlayerHurtOther(self):
        """ 玩家命中目标时触发 """
        pass

    def onLoadBefore(self):
        pass

    def onLoad(self):
        """ 状态成功被加载 """
        pass

    def getState(self):
        """ 获取状态情况 """
        return False

    def canChange(self, _=None):
        """ 如若当前状态持续中有其他状态加入将通过该方法计算是否允许切换到 如若成功切换触发onChange """
        return False

    def onChange(self):
        pass

    def onDyExit(self):
        """ 动态退出状态 不一定为onChange发起 也可能是主动抛出 """
        pass

    def onLoadErr(self):
        """ 失败性加载 """
        pass

    def exitSelf(self):
        """ 退出SELF状态 """
        pass
    
    def setATEStateQuery(self, value=0, clientUpdateNow=False):
        pass

    def setKLRender(self, state=True):
        pass

    def setQuery(self, value=0, clientUpdateNow=False):
        pass

class MODEL_AdvancedATEStateManager:
    """ 高级状态管理器 """
    def __init__(self):
        self.usingState = None
    
    def loadState(self, stateObj=MODEL_AdvancedATEState()):
        return True

    def getWorkState(self):
        """ 获取是否处于工作状态 """
        return False
    
    def getUsingObj(self):
        # type: () -> MODEL_AdvancedATEState | None
        """ 获取使用中的对象 """
        return self.usingState

    def tryCall(self, funcName=""):
        pass

    def exitAll(self):
        pass

    def deepExitAll(self):
        """ 深度退出所有状态 """
        pass

    def deepBreakAll(self):
        """ 深度打断所有情况 包括状态, 翻滚, 攻击, 蓄力 """
        pass

    def _log(self):
        pass

class MODEL_PlayerVitalityManager:
    """ 玩家体力管理器 """
    def __init__(self, minValue=-35, safeValue=100, maxOverflow=30, defaultValue=0):
        self.minValue = float(minValue)
        self.safeValue = float(safeValue)
        self.maxValue = float(safeValue + maxOverflow)
        self._value = float(defaultValue)
    
    def getInfiniteState(self):
        return False

    def onTickUpdate(self):
        pass

    def recharge(self, value=10):
        # type: (int | float) -> None
        """ 恢复指定系数的体力(负数时为消耗) """
        pass

    def getRenderRatio(self):
        # type: () -> float
        """ 获取渲染中的比率值 [0.0, 1.0] """
        pass

    def hasVitality(self, minValue=0.0):
        # type: (float) -> bool
        pass

    def useVitality(self, value=10.0):
        # type: (float) -> bool
        pass

class MODEL_PlayerEnergyManager(MODEL_PlayerVitalityManager):
    pass

class MODEL_HistoricalOptManager:
    """ 历史操作管理器 """
    def __init__(self):
        self._saveMap = {}  # type: dict[str, tuple[object, float]]

    def addHistorical(self, typeKey="default", value=1.0, saveTime=0.5):
        """ 添加历史数据 """
        pass

    def clearHistorical(self, typeKey="default"):
        """ 清除历史记录 """
        pass

    def equal(self, typeKey="default", value=1.0):
        """ 比较处理 """
        return True
    
    def use(self, typeKey="default", value=1.0):
        """ 比较 且若成功立即清除记录 """
        return True

    def hasKey(self, typeKey="default"):
        """ 是否存在该历史记录 """
        return True

    def anyUse(self, typeKey="default"):
        """ any比较 若存在则清理记录 """
        return True

class MODEL_TickLoopState(MODEL_AdvancedATEState):
    def __init__(self):
        MODEL_AdvancedATEState.__init__(self)
        self._ACATime = 0.0
        """ 自动延续攻击时间 若>0将在状态结束后延续普通攻击段数 """
        self._ACAINDEX = -1
        self._workingState = False
        self._tickValue = 0
        self._slowMove = False
        self.breakOpt = True

    def setMoveSlow(self, state=False):
        pass
    
    def setMoveOPTState(self, state=False):
        pass

    def onLoadBefore(self):
        pass

    def onLoad(self):
        pass

    def _onTick(self):
        pass
    
    def onFree(self):
        pass

    def onTick(self):
        pass

    def getState(self):
        return True

    def onDyExit(self):
        pass

class MODEL_QuickStrikeState(MODEL_TickLoopState):
    def __init__(self):
        MODEL_TickLoopState.__init__(self)
        self._signal = 0
        self._canChangeTypeCls = [] # type: list[type]
        self._needChange = False

    def getRpcCompName(self):
        return self.__class__.__name__
    
    def rpcSetSignal(self, value=0):
        """ 同rpcCompCall 区别是设置组件信号的同时对内缓存状态避免大量发包 """
        pass

    def CREATE_RANGE_VIBRATION_BLOCK(self, r=3, mutDir=3.0):
        pass
    
    def getParent(self):
        # type: () -> MODEL_QuickStrikeFunc
        """ 获取父节点切手技对象 """
        pass

    def getConfig(self):
        from ATE_MODEL import MODEL_BattleExpansionConfig
        return MODEL_BattleExpansionConfig

    def rpcCompCall(self, funcName="", *args, **kwargs):
        """ 远程调用服务端同名组件方法(需要确保使用addSelfStateComp创建) """
        pass

    def addStateComp(self, compName, *args):
        """ 添加状态组件 """
        pass
    
    def addSelfStateComp(self, *args):
        """ 添加自己同名定义的异端状态组件 """
        pass

    def removeStateComp(self, compName):
        """ 删除状态组件 """
        pass
    
    def removeSelfStateComp(self):
        """ 删除自己同名定义的异端状态组件 """
        pass

    def canChange(self, other):
        return False

class MODEL_QuickStrikeFunc(MODEL_UserOPTEvent):
    """ 切手技功能管理 """
    def __init__(self):
        self.useLongClick = False
        self._isLongTouchIng = False

    def getConfig(self):
        from ATE_MODEL import MODEL_BattleExpansionConfig
        return MODEL_BattleExpansionConfig

    def loadState(self, _state=MODEL_QuickStrikeState()):
        return False

    def onClick(self):
        pass

    def onLongClickStart(self):
        pass

    def onLongClickFree(self):
        pass

    def _onLongClickStart(self):
        pass

    def _onLongClickFree(self):
        pass

    def _onInteractiveOtherFree(self):
        pass

class MODEL_QuickStrikeManager:
    @staticmethod
    def regItemQuickStrike(itemName="", quickStrike=MODEL_QuickStrikeFunc()):
        """ 注册特定物品切手技 """
        pass

    @staticmethod
    def regTypeItemQuickStrike(typeName="", quickStrike=MODEL_QuickStrikeFunc()):
        """ 注册特定类型物品切手技 """
        pass

    @staticmethod
    def regCustomItemQuickStrike(customId=1, quickStrike=MODEL_QuickStrikeFunc()):
        """ 注册自定义物品切手技 """
        pass

    def __init__(self):
        self._lastQuickStrike = None    # type: MODEL_QuickStrikeFunc | None

    def getQuickStrike(self):
        # type: () -> MODEL_QuickStrikeFunc | None
        """ 获取当前使用中的切手技 """
        pass

    def _mallocQuickStrike(self):
        # type: () -> MODEL_QuickStrikeFunc | None
        """ 分配新的切手技 """
        pass

    def tryCall(self, funcName="", *args, **kwargs):
        pass

    def onClick(self):
        pass

    def onLongClickStart(self):
        pass

    def onLongClickFree(self):
        pass

class MODEL_CanBreakQuickStrike(MODEL_QuickStrikeState):
    """ 一种支持操作打断的切手技状态 """
    def canBreak(self):
        return False

    def onUserTryRoll(self):
        pass
    
    def onUserTryDefense(self):
        pass

    def onUserClickAttackButton(self):
        pass

class MODEL_OnceAttackQuickStrike(MODEL_CanBreakQuickStrike):
    """ 单次攻击 切手状态 """
    def __init__(self, attackData=None, bindQuery="", bindValue=200.0, useOffHand=False, useBodyDirHurt=False):
        from ATE_MODEL import MODEL_SkillAttackPreset
        MODEL_CanBreakQuickStrike.__init__(self)
        self.useBodyDirHurt = useBodyDirHurt
        self.useKLRender = True
        self.attackObj = MODEL_SkillAttackPreset(attackData, useOffHand=useOffHand, bindQuery=bindQuery, subValueId=bindValue-1)
        self.moveBreak = True

    def getState(self):
        return False
    
    def onLoad(self):
        pass
    
    def onBreakAT(self):
        pass

    def onStartAT(self):
        pass

    def onEndAT(self):
        pass

    def onHitAT(self):
        pass

    def onFree(self):
        pass

class MODEL_OnceBullyAttackQuickStrike(MODEL_OnceAttackQuickStrike):
    pass

# SERVER MODEL 以下部分依赖QuModLibs 此处只作简单的声明
class MODEL_QBaseEntityComp:
    pass

class MODEL_VEC3:
    pass

# 适用于 QuModLibs 的完整定义
# from ...QuModLibs.Math import Vec3
# from ...QuModLibs.Modules.EntityComps.Globals import _QBaseEntityComp

# class MODEL_QBaseEntityComp(_QBaseEntityComp):
#     pass

# class MODEL_VEC3(Vec3):
#     pass

class MODEL_BaseQuickStrikeState(MODEL_QBaseEntityComp):
    """ 基类切手技状态 """
    def __init__(self):
        self._signal = 0
        self._tickValue = 0
        self._engineTickValue = 0
        self._moveTimeLine = None
        self._motionTimeLineMove = None
        self._motionAbsMove = True

    def _setSignal(self, value=0):
        """ 信号设置 通常由客户端发起 """
        pass

    def setImmuneDamage(self, state=True):
        pass

    def setTimeLineMove(self, timeLine, absMove=True):
        pass

    def setMotionTimeLineMove(self, timeLine):
        """ 设置相对向量运动的时间线 相比setTimeLineMove它是经过插值运算的 """
        pass

    def updateMotionTimeLine(self):
        """ 更新向量时间线 """
        pass

    def setABSMotion(self, motion=(0, 0, 0)):
        """ 设置相对向量 """
        pass

    def setMotion(self, motion=(0, 0, 0)):
        pass

    def getMotion(self):
        return (0, 0, 0)

    def getBodyDirVc(self):
        # type: () -> MODEL_VEC3
        pass

    def addEffect(self, effectName="speed", duration=10, amplifier=0, showParticles=True):
        pass

    def playsound(self, soundName, volume=1.0, r=10):
        """ 基于命令的音频广播 """
        pass
    
    def putParticle(self, particle="", absPos=(0, 0, 0.4)):
        """ 基于命令的粒子广播 """
        pass

class MODEL_BaseDefenseQuickStrikeState(MODEL_BaseQuickStrikeState):
    """ 基类防御切手技状态 (自定义防御策略) """
    def __init__(self):
        MODEL_BaseQuickStrikeState.__init__(self)
        self._superDefenseCount = 0
        self.hurtArgs = {}

    def onHurt(self):
        return False

    def isEntityHurt(self):
        """ 检查受伤来源是不是实体直接攻击 """
        return False

    def isProjectileHurt(self):
        """ 检查受伤来源是不是抛掷物攻击 """
        return False

    def passHurt(self):
        """ 免疫单次伤害 """
        return 0

    def reduceDamage(self, mut=0.5, knock=False):
        """ 按百分比减免受到的伤害 """
        pass

    def getHurtSrcEntityId(self):
        """ 获取受伤来源实体ID """
        return "-1"

    def frontalAttackInspection(self):
        """ 正面伤害攻击检查(支持抛掷物/近战生物) """
        pass

    def bulletOpen(self):
        pass

    def superDefense(self, mutValue=0.65, knowBack=2.0, effectTime=5, playEffect=True):
        pass