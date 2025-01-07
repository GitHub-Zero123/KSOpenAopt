# KSOpenAopt 开放功能

KSOpenAopt 提供了适用于网易我的世界 KID动作优化/剑魂 的扩展(数据包) API/解决方案

后续将以 AOPT 简称 KID动作优化/剑魂

By Zero123 (2025/01/06)

## 自动化构建工具
BuildTools提供了适用于双AOPT的低代码扩展包构建解决方案 实现一次开发双MOD适配

### 开始构建
通过执行QBlockBuilder.exe即可开始构建工作 若无异常将在特定目录生成Addon包

### MANIFEST.json
适用于 QBlockBuilder 的构建配置清单表，详细可查阅 [QBlockBuilder](https://gitee.com/bili_zero123/QBlockBuilder) 通用构建系统

```json
{
    "package": "test_package",  // 应修改为您的项目名(需遵循命名规范 推荐小写下划线命名)
    "jsonOptimize": true,
    "pyReload": true,
    // "debug": false,
    // "addon++": false,
    "modules": [
        // 添加两个.dll文件引用同一个目录(aopt/*), 可以同时支持KID和剑魂的构建
        {
            "lib": "libs/KAOBuildLib",
            "path": "aopt",     // 配置path目录 提供Build支持
            "description": "[v1.0.0] KID动作优化扩展包构建支持"
        },
        {
            "lib": "libs/SAOBuildLib",
            "path": "aopt",
            "description": "[v1.0.0] 剑魂扩展包构建支持"
        },
        {
            "lib": "libs/CheckAOPT",
            "description": "用于生成运行时的前置环境检查(KID动作优化/剑魂), 如果不存在则弹出提示"
        }
    ]
}
```

### 自定义默认皮肤
在path目录(aopt/*.json)创建任意名称的json文件(允许中文)并声明其类型为 custom_skin
```json
// 自定义皮肤.json
{
    "type": "custom_skin",  // 类型声明
    "skin_name": "这是一个测试皮肤",
    // "skin_id": "test1", // 在不指定skin_id的情况下会自动分配
    "icon": "apple.png",    // 皮肤渲染的头像
    "texture": "apple.png"  // 皮肤纹理(64x64)
    // "skin_type": "slim" // 可选参数, 如果不指定则默认为粗手模型
}
```
该构建库支持 相对与绝对目录(自path起始)的文件访问 但不支持无后缀引用/向上的相对引用

### 自定义3D外观(自由模型)
在path目录(aopt/*.json)创建任意名称的json文件(允许中文)并声明其类型为 custom_3d_skin
```json
{
    "type": "custom_3d_skin",   // 类型声明
    "skin_name": "这是一个3D的皮肤",
    "icon": "apple.png",      // 完整目录引用
    "texture": "apple2.png",  // 相对目录引用
    "geometry": "geometry.test_model",
    // [选填] 面部表情渲染 默认禁用, 可显性开启 该参数对剑魂不生效
    "allow_face_expressions": true,
    // [选填] 默认动画播放(持续循环) 用于调整模型细节亦或者动画表现 现阶段仅开放单个自定义动画参数
    "default_animation": "animation.armor_stand.brandish_pose"

    /*
        模型规范: Models/3d_model.json
        考虑到剑魂兼容问题 无论是否需要KID面部表情 都应设计面部模型
        特殊: 因KID动作优化历史实现问题 部分Bones不得缺少(用于实时位置定位优化动画表现) 否则可能出现动画异常
        建议: 直接在该模型模板上修改 不需要的Bone清空模型块但保留组
    */
}
```
该构建库同时也支持 动画/模型(1.12+) 的直接放置(任意位置) 在构建环节会被自动复制移动到Addon的目标位置

### 自定义刀光纹理
在path目录(aopt/*.json)创建任意名称的json文件(允许中文)并声明其类型为 custom_sword_trail_textures
```json
{
    "type": "custom_sword_trail_textures",
    "textures": [
        "apple.png",    // 完整路径查找
        "test2.png"
        // ...
    ]
}
```

### 自定义常态攻击动作(ATE)
截至当前版本 仅支持普通连续攻击自定义 蓄力/跳劈/翻滚技暂不支持 或将在未来逐步开放
```json
// 类型为 default_attack
// 若非特殊说明 所有带有默认值的参数都可以选填/不填
// 标准部分理应被双AOPT一致性支持 非标准部分可能因具体运行环境而定义
{
    "type": "default_attack",
    "ate_id": "custom_attack_1",  // 必填 否则构建时抛出异常警告
    "ate_name": "常态攻击",       // [标准] 当ate_name不填时默认使用ate_id
    "default_items": [],         // 选填 若定义可为特定物品默认添加此攻击预设
    "attack_type": "default",    // 默认default 可选random(将随机选择子节点攻击)
    "custom_sounds": {},         // [标准] 选填 自定义sounds到玩家资源(多个MOD相同的键位名会互相覆盖 若非重复资源请尽可能避免重复键名)
    // rt_参数由构建系统生成 (以下参数仅为python层提供 非用户数据)
    // "rt_bind_query": "query.mod.xxx",            // [标准] rt_bind_query必定会被生成 用于控制攻击下标 0为终止
    // "rt_anim_load": "ks_aopt_{&ate_id}_root",    // [标准] rt_anim_load的动画控制器key理应持续工作 以便及时混合动画
    // "rt_anims_kv": {                             // [标准] rt_anims_kv静态初始化资源 应全部加载到玩家(包含控制器与动画)
    //     "ks_aopt_{&ate_id}_root": "controller.animation.ks_aopt_{&ate_id}"
    // },
    "attack_childs": [
        {
            // 必填参数
            "attack_time": 2.0,     // 描述整个攻击的持续时间(超过该时间视为自然结束 无法继续衔接下一个child)
            "can_break_time": 0.5,  // 描述攻击从x秒开始可以被打断衔接到下一个child
            "anim_time": 0.5,       // 描述有效动画时间 若非移动打断动作 超过该时间也会打断并回到待机动画(不代表攻击结束 以attack_time为准) 若缺省默认同步can_break_time
            // 选填参数
            "play_anims": ["animation.xxx", "animation.xxx2"],     // 攻击动画播放 可选list[str] | str
            "hit_time_line": {
                "0.0": {
                    "type": "front_aoe",    // 默认front_aoe 可选front_aoe, aoe
                    "range": 2,             // 攻击半径 选填 默认3
                    "hurt_mut": 1.8,        // 攻击伤害倍率 选填 默认1
                    "hurt_vec": [0, 0, 0],  // [标准] 选填默认[0, 0, 0]不作击退向量处理 允许使用单个float自动构造[0, 0, v]
                    "break_block": false,   // [标准] 默认false 是否破坏方块(裂地)
                    "args": {}              // 非标准传递参数 具体处理由具体运行环境决定
                }
            },
            "cmd_time_line": {
                "0.5": [    // [标准] 可选 str | list[str]
                    "/say 唱跳RAP",
                    // [标准] 仅/开头为指令执行 其他关键字则代表其他功能(待定)
                    "/say 我是雪豹"
                ]
            },
            "blockbench": false,        // [标准] 默认false 声明使用blockbench模式 若为true move_time_line的z轴将反向解析 同时移动单位将按像素(16=1格)处理
            "stop_mot_when_end": false, // [标准] 默认false 声明为true将会自动在动作结束时重置当前瞬时速度 可避免滑动(依情况使用)
            "lock_pos_y": false,        // [标准] 默认false 是否锁定y轴位置 若声明为true move_time_line将严格处理y轴位置(y轴的0数据 false模式下混合重力加速度)可实现滞空
            "move_time_line": {
                // [标准] 支持list[float, float, float] | float 当使用单一数值float 运行时将自动构造[0, 0, v]
                "0.0": [0, 0, 0],
                "0.2": [0, 0, 0]
            }
        },
        {
            // ...
        }
    ]
}

// Models/work_model.json 提供了动画开发模型标准

```
其中 animations 资源可以直接放置在构建PATH中也可以放置在src/{RES_PACK}/animations中


注意: 构建系统并不会为您重命名 animations 因此需要注意多MOD的重名问题 建议搭配作者/项目名作为前缀

## (进阶) Api 接入

MOD_API 提供了适用于 KID/剑魂的开放性接口，用户可在判断 hasMod 后调用相关功能

### 原生 MOD 项目

建议监听 `LoadClientAddonScriptsAfter` 事件并在判断存在 AOPT 后操作（部分接口有特殊说明）

```python
# -*- coding: utf-8 -*-
import mod.client.extraClientApi as clientApi
from KID_OpenSdk.ClientAPI import KAPI
ClientSystem = clientApi.GetClientSystemCls()

class MySystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        self.ListenForEvent(
            clientApi.GetEngineNamespace(),
            clientApi.GetEngineSystemName(),
            "LoadClientAddonScriptsAfter", self,
            self.LoadClientAddonScriptsAfter
        )
    
    def LoadClientAddonScriptsAfter(self, _={}):
        if KAPI.hasMod():
            ...
```

### QuMod 项目

可直接在 `modMain.py` 中判断处理（1.3.3+）

```python
# -*- coding: utf-8 -*-
from QuModLibs.QuMod import *
MOD = EasyMod()

@PRE_CLIENT_LOADER_HOOK
def QRT_KID_API():
    from KID_OpenSdk.ClientAPI import KAPI
    if KAPI.hasMod():
        MOD.Client("KAOPT_RT")
```

详细功能请自行查阅相关python文件定义 亦或者联系相关开发者咨询