# -*- coding: utf-8 -*-
USE_GLR_RENDER = True
""" 使用GLR渲染系统加载玩家资源 """

USE_GLR_QUERY_SYSTEM = True
""" 使用GLR处理节点系统 """

USE_DELAY_CALL = True
""" 使用延迟发包改善体验(适用于大多场景) """

USE_CLIENT_STATIC_RES = True
""" 使用客户端静态方案(仅GLR) """

QueryStartName = "query.mod.kid_ultra_"
""" 节点前缀 """

class CustomQuery:
    """ 自定义节点 """
    IsFlying = QueryStartName + "is_flying"                             # query.mod.kid_ultra_is_flying
    """ 检测 玩家飞行 """

    KeyBoardLeRiWard = QueryStartName + "keyboard_left_right_ward"      # query.mod.kid_ultra_keyboard_left_right_ward(1.0:右 -1.0:左)
    """ 检测 玩家左右按键 """

    KeyBoardForBackWard = QueryStartName + "keyboard_for_back_ward"     # query.mod.kid_ultra_keyboard_for_back_ward(1.0:前 -1.0:后)
    """ 检测 玩家前后按键 """
    
    CustomRideQuery = QueryStartName + "custom_ride_query"              # query.mod.kid_ultra_custom_ride_query
    """ 检测 自定义骑乘节点 """
    
    MainHandBlockType = QueryStartName + "main_hand_block_type"         # query.mod.kid_ultra_main_hand_block_type
    """ 检测 手持方块类型 """

    GetHoldItemsSlotId = QueryStartName + "hold_items_slot_id"          # query.mod.kid_ultra_hold_items_slot_id
    """ 检测 获取玩家物品栏id """

    GetEnchantType = QueryStartName + "enchant_type"                    # query.mod.kid_ultra_enchant_type(30.0:激流)
    """ 检测 获取玩家手持物品附魔类型 """

    ShoulderItem = QueryStartName + "shoulder_item"          # query.mod.kid_ultra_shoulder_item
    """ 返回背肩物品映射值 0代表无 """

    ShoulderItemEnc = QueryStartName + "shoulder_item_enc"   # query.mod.kid_ultra_shoulder_item_enc
    """ 返回背肩物品附魔状态 返回0/1 1代表附魔 """

    AttackModeType = QueryStartName + "attack_mode_type"                # query.mod.kid_ultra_attack_mode_type
    """ 战斗机制类型(描述处于哪一类战斗状态) """

    AttackState = QueryStartName + "attack_state"
    """ 战斗状态 正数代表多段攻击的哪一段 负数代表其他状态如翻滚 防御 """    # query.mod.kid_ultra_attack_state

    BattleExpansionState = QueryStartName + "battle_expansion_state"    # query.mod.kid_ultra_battle_expansion_state
    """ 战斗机制状态 """

    NewCustomCape = QueryStartName + "custom_cape"                      # query.mod.kid_ultra_custom_cape
    """ 新自定义披风 """

    NewCustomModelScale = QueryStartName + "model_scale"                      # query.mod.kid_ultra_model_scale
    """ 模型外观大小 """

    NewCustomModel = QueryStartName + "custom_model"                    # query.mod.kid_ultra_custom_model
    """ 新自定义模型 """

    NewCustomInter = QueryStartName + "custom_inter"                      # query.mod.kid_ultra_custom_inter
    """ 新自定义交互 """

    itemCustomQueryStand = QueryStartName + "state_ground_stand_custom"                    # query.mod.kid_ultra_state_ground_stand_custom
    """ 自定义动画——待机 """

    itemCustomQueryWalk = QueryStartName + "state_ground_walk_custom"                    # query.mod.kid_ultra_state_ground_walk_custom
    """ 自定义动画——移动 """

    itemCustomQuerySprint = QueryStartName + "state_ground_sprint_custom"                    # query.mod.kid_ultra_state_ground_sprint_custom
    """ 自定义动画——奔跑 """

    itemCustomQuerySneak = QueryStartName + "state_ground_sneak_custom"                    # query.mod.kid_ultra_state_ground_sneak_custom
    """ 自定义动画——潜行 """

    itemCustomQuerySneakMove = QueryStartName + "state_set_custom"                    # query.mod.kid_ultra_state_set_custom
    """ 自定义动画——默认配置 """

    itemCustomQueryScale = QueryStartName + "items_scale_custom"                    # query.mod.kid_ultra_items_scale_custom
    """ 自定义动画——武器大小 """

    # itemCustomQueryCharge = QueryStartName + "charge_custom"                    # query.mod.kid_ultra_charge_custom
    # """ 自定义动画——蓄力 """

    itemCustomQueryDefence = QueryStartName + "defence_custom"                    # query.mod.kid_ultra_defence_custom
    """ 自定义动画——防御 """    
    
    itemCustomQueryFightEND = QueryStartName + "fight_end_custom"                    # query.mod.kid_ultra_fight_end_custom
    """ 自定义动画——收刀 """

    itemCustomQueryDefence = QueryStartName + "trail_custom"                    # query.mod.kid_ultra_trail_custom
    """ 自定义动画——拖尾位置 """

    localUiPage = QueryStartName + "local_ui_page"                                  # query.mod.kid_ultra_local_ui_page
    """ 本地UIPageID """

    damageReduction = QueryStartName + "max_damage_reduction"                       # query.mod.kid_ultra_max_damage_reduction
    """ 防御当前最大防御消减值 >0时代表处于防御状态(非int 存在区间值) """

    defenseHurtTime = QueryStartName + "defense_hurt_time"                          # query.mod.kid_ultra_defense_hurt_time
    """ 返回最后一次防御受伤触发时间 """

    defenseRatio = QueryStartName + "defense_ratio"                                 # query.mod.kid_ultra_defense_ratio
    """ 返回最后一次防御比率 1.0即完美防御 """

    globalLastHurtTime = QueryStartName + "global_last_hurt_time"                   # query.mod.kid_ultra_global_last_hurt_time
    """ 玩家全局最后一次受伤时间 """

    newCustomCamera = QueryStartName + "new_custom_camera"                          # query.mod.kid_ultra_new_custom_camera
    """ 新自定义摄像机 """

    customATEId = QueryStartName + "custom_ate_id"                                  # query.mod.kid_ultra_custom_ate_id
    """ [信号节点] 用于通知python代码调用对应的自定义ATE (也可以用于判断当前使用的自定义ATE) """

    modUseCustomModel = QueryStartName + "mod_use_custom_model"                     # query.mod.kid_ultra_mod_use_custom_model
    """ mod扩展 使用自定义模型形象 """

    modUseCustomSkin = QueryStartName + "mod_use_custom_skin"                       # query.mod.kid_ultra_mod_use_custom_skin
    """ mod扩展 使用自定义纹理形象 """

    modDisRenderFace = QueryStartName + "mod_dis_render_face"                       # query.mod.kid_ultra_mod_dis_render_face
    """ mod扩展 是否禁用面部表情渲染 """

    # modHideArmor = QueryStartName + "mod_hide_armor"                                # query.mod.kid_ultra_mod_hide_armor
    # """ mod扩展 是否隐藏盔甲 """

    ateAttackMode = QueryStartName + "ate_attack_mode"                            # query.mod.kid_ultra_ate_attack_mode
    """ 返回ATE攻击模式 0.限制移动 1.走A模式 """

    ateKLColorMode = QueryStartName + "ate_kl_color"                                # query.mod.kid_ultra_ate_kl_color
    """ ate刀光色彩模式 """

    offHandAteKLColorMode = QueryStartName + "off_ate_kl_color"                     # query.mod.kid_ultra_off_ate_kl_color
    """ 副手Ate刀光色彩模式 """

    blockAllAnims = QueryStartName + "block_all_anims"                              # query.mod.kid_ultra_block_all_anims
    """ 屏蔽所有动画 """

    offHandAteMode = QueryStartName + "off_hand_ate_id"                             # query.mod.kid_ultra_off_hand_ate_id
    """ 副手ATE模式设置 """

    ateKLScale = QueryStartName + "ate_kl_scale"                                    # query.mod.kid_ultra_ate_kl_scale
    """ ATE刀光大小 """

    ateRollId = QueryStartName + "ate_roll_id"                                      # query.mod.kid_ultra_ate_roll_id
    """ 翻滚ID 0.None 1.前翻 2.后翻 3.左侧翻 4.右侧翻 11.前闪避 12.后闪 13.左闪 14.右闪 """

    advancedATEState = QueryStartName + "ate_advanced_state"                        # query.mod.kid_ultra_ate_advanced_state
    """ 高级ATE状态 0.无 1.小僵值 2.大僵值 20-100保留技能位 负数保留自定义扩展 """

    ateQuickStrikeId = QueryStartName + "ate_quick_strike"                          # query.mod.kid_ultra_ate_quick_strike
    """ 描述当前使用了哪一种切手技 """

    KIDCustomButton_1 = QueryStartName + "custom_button_1"
    """ 全局动画设置 原版向位移 四向位移 """                                          # query.mod.kid_ultra_custom_button_1

    KIDCustomButton_2 = QueryStartName + "custom_button_2"
    """ 全局动画设置 原版向跳跃 强制覆盖跳跃动画 """                                          # query.mod.kid_ultra_custom_button_2

    KIDCustomButton_3 = QueryStartName + "custom_button_3"
    """ 全局动画设置 保留待机动画 取消待机动画 """                                          # query.mod.kid_ultra_custom_button_3