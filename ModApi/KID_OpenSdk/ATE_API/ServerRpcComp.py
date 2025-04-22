# -*- coding: utf-8 -*-
from ..ServerAPI import kapi
from STATE_MODEL import MODEL_BaseQuickStrikeState, MODEL_BaseDefenseQuickStrikeState, MODEL_VEC3
lambda: "By Zero123 该模块包含完整的组件类引用 请确保前置正确加载否则将产生异常"

_SERCOMP = kapi.impModFile("BattleExpansion.COMPS.Server")
_ServerStateRPC = kapi.impModFile("Modules.PlayerStates.ServerStateRPC")

def GET_BODY_DIR_VC(entityId):
    # type: (str) -> MODEL_VEC3
    return _SERCOMP.GET_BODY_DIR_VC(entityId)

BaseQuickStrikeState = _SERCOMP.BaseQuickStrikeState  # type: type[MODEL_BaseQuickStrikeState]
BaseDefenseQuickStrikeState = _SERCOMP.BaseDefenseQuickStrikeState  # type: type[MODEL_BaseDefenseQuickStrikeState]

def regCustomQuickState(stateName, stateCls):
    # type: (str, type) -> None
    _ServerStateRPC.REG_STATE_COMP(stateName, stateCls)