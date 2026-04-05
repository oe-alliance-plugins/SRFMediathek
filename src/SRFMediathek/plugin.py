# -*- coding: UTF-8 -*-
from Plugins.Plugin import PluginDescriptor
from importlib import reload


def main(session, **kwargs):
    from . import srf

    reload(srf)
    session.open(srf.SRFMediathek)


def Plugins(**kwargs):
    return PluginDescriptor(name="SRF Mediathek", description="SRF Mediathek Plugin für Enigma2", where=[PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU], icon="logo.png", fnc=main)
