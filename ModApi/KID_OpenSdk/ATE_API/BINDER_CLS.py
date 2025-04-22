# -*- coding: utf-8 -*-
from ..ClientAPI import OO_MCLS_REF
from ATE_MODEL import MODEL_AttackData
lambda: "By Zero123 该模块包含完整的KID新式绑定类引用 请确保前置正确加载否则将产生异常"
_aoptClient = "Modules.PlayerOPT.Client"

@OO_MCLS_REF.bindTarget("BattleExpansion.SystemClient")
class AttackData(MODEL_AttackData):
    pass

class TimerLoaderDefine:
    class Timer:
        def __init__(self, callObject, argsTuple = tuple(), kwargsDict = dict(), time = 0.0, loop = False):
            # type: (object, tuple, dict, float, bool) -> None
            self.callObject = callObject
            self.argsTuple = argsTuple
            self.kwargsDict = kwargsDict
            self.loop = loop
            self.setTime = time
            self.valueTime = time
            self._cacheUpdateTime = 0.0

        def call(self):
            pass

        def copy(self):
            # type: () -> TimerLoaderDefine.Timer
            pass

        def rest(self):
            pass

    def _clearAllTimer(self):
        pass

    def addTimer(self, timer):
        return False
    
    def removeTimer(self, timer):
        return False

    def _timerUpdate(self, updateTime=0.033):
        pass

@OO_MCLS_REF.bindTarget(_aoptClient)
class AttackBindHandler(TimerLoaderDefine):
    def __init__(self):
        TimerLoaderDefine.__init__(self)
        self.disOldMoveLine = False
        self.disOldHurtLine = False
        self.minAttackTime = 0.0
        self.maxAttackTime = 999.0
        self.attackSpeed = 1.0

    def onAttackStart(self):
        pass

    def onAttackEnd(self):
        pass

    def onAttackUpdate(self):
        pass

    def onMoveBreak(self):
        pass

@OO_MCLS_REF.bindTarget(_aoptClient)
class RPCAttackBindHanlder(AttackBindHandler):
    def __init__(self, *args, **kwargs):
        AttackBindHandler.__init__(self)
        self.packArgs = args
        self.packKwArgs = kwargs

    def getRPCName(self):
        return self.__class__.__name__

    def getRPCId(self):
        return id(self)

    def getPackArgs(self):
        return self.packArgs

    def getPackKwArgs(self):
        return self.packKwArgs

    def onAttackStart(self):
        pass

    def onAttackEnd(self):
        pass

@OO_MCLS_REF.bindTarget(_aoptClient)
class RPCAttackSpeedLine(RPCAttackBindHanlder):
    """ 混合攻击速度的RPC时间线类 """
    pass

# 内置实现类
@OO_MCLS_REF.bindTarget(_aoptClient)
class RPCServerLineMove(RPCAttackSpeedLine):
    """ 服务端实现的线性移动类 """
    def __init__(self, moveVcLine={}, blockBenchMode=False, unit=16, forceY=False, stopMotWhenEnd=False, **_):
        """
            TIPS: 服务端版本缺少客户端数据信息 不支持碰撞检查, 走A模式等功能

            @moveVcLine 移动位置时间线(位置非速度)
            @blockBenchMode 启用后反转z轴
            @unit 标准单位量 默认16为一米
            @forceY 强制Y轴 默认为False 启用后可以实现滞空
            @stopMotWhenEnd 默认为False 启用后在时间线结束后立即停止当前的剩余瞬时速度
            @highp 废弃参数不作使用
        """
        RPCAttackBindHanlder.__init__(self, moveVcLine, blockBenchMode, unit, forceY, stopMotWhenEnd)

@OO_MCLS_REF.bindTarget(_aoptClient)
class RPCServerLoopMove(RPCAttackSpeedLine):
    """ 服务端实现的持续移动类 将持续向前方移动 """
    def __init__(self, moveVec=[0, 0, 0.5]):
        # type: (list[float] | float) -> None
        RPCAttackSpeedLine.__init__(self, moveVec)

@OO_MCLS_REF.bindTarget(_aoptClient)
class NewLineMove(AttackBindHandler):
    def __init__(self, moveVcLine={}, blockBenchMode=False, unit=16, forceY=False, stopMotWhenEnd=False, highp=4, useInMoveAttack=False):
        # type: (dict, bool, int, bool, bool, bool, bool) -> None
        """
            @moveVcLine 移动位置时间线(位置非速度)
            @blockBenchMode 启用后反转z轴
            @unit 标准单位量 默认16为一米
            @forceY 强制Y轴 默认为False 启用后可以实现滞空
            @stopMotWhenEnd 默认为False 启用后在时间线结束后立即停止当前的剩余瞬时速度
            @highp 默认为4 高精度位置同步越低频率越高(有一定的性能开销)
            @useInMoveAttack 强制在走A模式下加载逻辑
        """
        AttackBindHandler.__init__(self)

@OO_MCLS_REF.bindTarget(_aoptClient)
class NewTimeLineHurt(AttackBindHandler):
    def __init__(self, hurtTimeLine={}):
        # type: (dict[float | str, AttackData]) -> None
        AttackBindHandler.__init__(self)
    
    def getMinAttackTime(self):
        return 0.0

    def loadHurtData(self, attackData):
        # type: (AttackData) -> None
        pass

@OO_MCLS_REF.bindTarget(_aoptClient)
class LoopTimeLineHurt(NewTimeLineHurt):
    pass

@OO_MCLS_REF.bindTarget(_aoptClient)
class NewCmdTimeLine(AttackBindHandler):
    def __init__(self, timeLine={}):
        # type: (dict[float | str, str | list[str]]) -> None
        AttackBindHandler.__init__(self)

@OO_MCLS_REF.bindTarget(_aoptClient)
class CustomHitSoundsLine(AttackBindHandler):
    """ 自定义命中音效时间线 """
    def __init__(self, soundLine={}, autoRest=True):
        # type: (dict[str | float, str | None] | str | None, bool) -> None
        AttackBindHandler.__init__(self)

@OO_MCLS_REF.bindTarget(_aoptClient)
class CustomHitParLine(AttackBindHandler):
    """ 自定义命中特效时间线 """
    def __init__(self, parLine={}, autoRest=True):
        # type: (dict[str | float, str | None | tuple[str, float]] | str | None | tuple[str, float], bool) -> None
        # CustomHitParLine("par")
        # CustomHitParLine({0.0: "par", 0.1: "par2"})
        # CustomHitParLine({0.0: "par", 0.1: ("par2", 0.5)})
        AttackBindHandler.__init__(self)

@OO_MCLS_REF.bindTarget(_aoptClient)
class SwordSlippedTimeLine(AttackBindHandler):
    """ 收刀状态时间线(适用于拔刀出鞘类动作) """
    def __init__(self, stateLine={}, autoRest=True):
        # type: (dict[str | float, bool] | float, bool) -> None
        """
            @stateLine 状态时间线 允许使用{0.5: True, 0.8: False, ...}详细控制 或者 单时间控制 SwordSlippedTimeLine(0.5) (等价于SwordSlippedTimeLine({0.5: True}))
            @autoRest 是否自动重置状态 默认为True 将在结束时自动重置收刀状态为False
        """
        AttackBindHandler.__init__(self)

@OO_MCLS_REF.bindTarget(_aoptClient)
class RPCInvincibleFrameTimeLine(RPCAttackSpeedLine):
    """ 无敌帧时间线 """
    def __init__(self, invTimeLine={}):
        # type: (dict[str | float, bool] | float, bool) -> None
        """
            @invTimeLine 无敌帧时间线 允许使用{0.5: True, 0.8: False, ...}详细控制 或者 单时间控制 RPCInvincibleFrameTimeLine(0.5) (等价于RPCInvincibleFrameTimeLine({0.5: True}))
            该功能类由服务端处理 无论如何在攻击结束时都会重置无敌帧
        """
        RPCAttackSpeedLine.__init__(self)

@OO_MCLS_REF.bindTarget(_aoptClient)
class CustomStateQueryLine(AttackBindHandler):
    """ 自定义状态绑定时间线 """
    def __init__(self, bindQuery, stateLine, autoRest=True):
        # type: (str, dict[str | float, float], bool) -> None
        AttackBindHandler.__init__(self)

@OO_MCLS_REF.bindTarget(_aoptClient)
class LockQueryStateLine(CustomStateQueryLine):
    """ 锁定Query状态时间线 """
    def __init__(self, bindQuery, stateLine, autoRest=True):
        CustomStateQueryLine.__init__(self, bindQuery, stateLine, autoRest)
        self.lockValue = None

@OO_MCLS_REF.bindTarget(_aoptClient)
class DisAttackSpeedState(AttackBindHandler):
    """ 禁用AttackSpeed状态声明 """
    def __init__(self, state=True):
        AttackBindHandler.__init__(self)
        self.disAttackSpeed = state