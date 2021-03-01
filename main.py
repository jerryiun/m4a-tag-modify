#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

from mutagen.mp4 import MP4
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

'''
m4a歌曲 标签歌词去掉方括号中的时间
'''
if __name__ == "__main__":

    os.chdir('D:/music')
    input_dir = os.getcwd()

    failed = []
    for file in os.listdir(unicode(input_dir, 'utf-8')):
        if file.split('.')[-1] == 'm4a':
            try:
                audio = MP4(file)
                for item in audio.tags:
                    if item == "\xa9lyr":  # lyrics
                        lyrics = audio.tags[item]
                        new_lyrics = re.sub(r'\[.*\]\n?', '', lyrics[0])  # 正则匹配替换[]内内容

                        audio.tags[item] = [new_lyrics]
                audio.save()
            except Exception, e:
                failed.append(file)
                continue

    # 编辑失败的文件
    if len(failed) > 0:
        print 'modify failed：'
        for f in failed:
            print f
