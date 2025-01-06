# -*- coding: utf-8 -*-
import mod.client.extraClientApi as clientApi

def RegisterKnifeLight(knifeLightList):
    Config = clientApi.ImportModule("SwordSoulScripts.Config")
    for knifeLight in knifeLightList:
        Config.KnifeLightTextureData.append([knifeLight])

def RegisterSkin(skin_id, name=None, icon="", texture=""):
    if not name:
        name = skin_id
    Config = clientApi.ImportModule("SwordSoulScripts.Config")
    Data = {
        "skin_id": skin_id,
        "name": name,
        "icon": icon,
        "texture": texture,
        "geometry": "geometry.better_player",
        "default_animation": ""
    }
    Config.ModelData.append(Data)

def RegisterModel(skin_id, name=None, icon="", texture="", geometry="", default_animation=""):
    if not name:
        name = skin_id
    Config = clientApi.ImportModule("SwordSoulScripts.Config")
    Data = {
        "skin_id": skin_id,
        "name": name,
        "icon": icon,
        "texture": texture,
        "geometry": geometry,
        "default_animation": default_animation
    }
    Config.ModelData.append(Data)

def HasSwordSoul():
    return clientApi.ImportModule("SwordSoulScripts.__init__")
