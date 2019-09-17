#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 51memo_v0.24.py
# A memo demo 51备忘录 添加智能识别，并用不同的颜色显示
# author: wanshican

import re
from color_me import ColorMe

__author__ = 'wanshican'

desc = '51备忘录'.center(30, '-')
print(desc)
welcome = 'welcome'
print(f'{welcome}', __author__)
print('请输入备忘信息：')


all_memo = []
is_add = True
all_time = 0
time_dict = {'中午': '12:00', '早上': '6:00', '上午': '9:00', '晚上': '20:00'}

RE_TIME = re.compile(r'(\d+)点')
RE_NOON = re.compile(r'中午|早上|上午|晚上')

while(is_add):
    info = input('请输入事件：')
    if RE_TIME.findall(info):
        in_time = RE_TIME.findall(info)[0]
        in_thing = info[info.find('点') + 1:]
    elif RE_NOON.findall(info):
        in_time = time_dict[RE_NOON.findall(info)[0]]
        in_thing = info[info.find('时') + 1:]
    else:
        print('输入格式有误，请重新输入！')
        continue

    print('待办列表'.center(30, '-'))
    one = {}
    one['时间'] = in_time
    one['事件'] = in_thing
    all_memo.append(one)

    num = 0
    for m in all_memo:
        num += 1
        print(num, end='\t')
        print(ColorMe().blue('时间：'), ColorMe().blue(str(m['时间'])), end='\t')
        print(ColorMe().red('事件：'), ColorMe().red(str(m['事件'])))

    print(f'共{len(all_memo)}条待办事项。', end='')
    print('(y:继续添加，n:退出)')
    is_add = input().strip() == 'y'
