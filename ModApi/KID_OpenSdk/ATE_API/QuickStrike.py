# -*- coding: utf-8 -*-
from ..ClientAPI import kapi, OO_MCLS_REF
from STATE_MODEL import (
    MODEL_UserOPTEvent,
    MODEL_AdvancedATEState,
    MODEL_TickLoopState,
    MODEL_QuickStrikeState,
    MODEL_QuickStrikeFunc,
    MODEL_CanBreakQuickStrike,
    MODEL_OnceAttackQuickStrike,
    MODEL_OnceBullyAttackQuickStrike,
)
from ATE_MODEL import MODEL_BattleExpansionConfig, MODEL_AttackData
lambda: "By Zero123 该模块包含完整的KID状态类引用 请确保前置正确加载否则将产生异常"

_stateDefineModule = "Modules.PlayerStates.StateDefine"
_StateDefine = kapi.impModFile(_stateDefineModule)

@OO_MCLS_REF.bindTarget("BattleExpansion.SystemClient")
class AttackData(MODEL_AttackData):
    pass

@OO_MCLS_REF.bindTarget(_stateDefineModule)
class UserOPTEvent(MODEL_UserOPTEvent):
    pass

@OO_MCLS_REF.bindTarget(_stateDefineModule)
class AdvancedATEState(MODEL_AdvancedATEState):
    pass

@OO_MCLS_REF.bindTarget(_stateDefineModule)
class TickLoopState(MODEL_TickLoopState):
    pass

@OO_MCLS_REF.bindTarget(_stateDefineModule)
class QuickStrikeState(MODEL_QuickStrikeState):
    pass

@OO_MCLS_REF.bindTarget(_stateDefineModule)
class QuickStrikeFunc(MODEL_QuickStrikeFunc):
    pass

@OO_MCLS_REF.bindTarget(_stateDefineModule)
class CanBreakQuickStrike(MODEL_CanBreakQuickStrike):
    pass

@OO_MCLS_REF.bindTarget(_stateDefineModule)
class OnceAttackQuickStrike(MODEL_OnceAttackQuickStrike):
    pass

@OO_MCLS_REF.bindTarget(_stateDefineModule)
class OnceBullyAttackQuickStrike(MODEL_OnceBullyAttackQuickStrike):
    pass

def GET_BATTLE_CONFIG():
    # type: () -> MODEL_BattleExpansionConfig
    """ 获取战斗Config """
    return _StateDefine.GET_BATTLE_CONFIG()