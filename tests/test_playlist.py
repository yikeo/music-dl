#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: HJK
@file: test_addon_netease.py
@time: 2019-06-10
"""

from music_dl import config
from music_dl.source import MusicSource
import os
import shutil


def test_playlist():
    config.init()
    config.set('outdir', 'E:\\My Documents\\My Musics\\')
    config.set('lyrics', True)
    config.set('source', 'netease')
    config.set('playlist', 'https://music.163.com/playlist?id=2909967264&userid=52794579')

    ms = MusicSource()
    songs_list = ms.playlist(config.get("playlist"))
    for idx in songs_list:
        idx.download()

    assert songs_list is not None


def test_filename():
    parent = "E:\\My Documents\\My Musics\\"
    for s in os.listdir(parent):
        if "、" in s:
            print(s)
            s2 = parent + s.replace('、', ',')
            s = parent + s
            if os.path.exists(s2):
                os.remove(s)
            else:
                shutil.move(s, s2)
        if "（1）" in s or "(1)" in s:
            print(s)
            s = parent + s
            os.remove(s)
    pass
