#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# guess21.py
# author: wanshican

import random
'''
游戏规则
两个玩家，游戏开始先输入名字
用字典保存每个玩家的信息：姓名，获胜次数
电脑随机产生两个数，每个玩家轮流猜一个数，与电脑随机两个数求和，最接近21的获胜
每轮结束显示玩家信息
按q退出游戏
'''

target = 21
user1 = input('第一个玩家名字：')
user2 = input('第二个玩家名字：')

users = {
    user1: {'win': 0},
    user2: {'win': 0}
}

while True:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    user1_guess = input(f'{user1} guess:')
    user2_guess = input(f'{user2} guess:')
    user1_sum = num1 + num2 + int(user1_guess)
    user2_sum = num1 + num2 + int(user2_guess)

    if abs(user1_sum - 21) > abs(user2_sum - 21):
        print(f'{user2} win!')
        users[user2]['win'] += 1
    else:
        print(f'{user1} win!')
        users[user1]['win'] += 1
        
    print('{}赢了{}次，{}赢了{}次'.format(user1, users[user1]['win'], user2, users[user2]['win']))
    tips = input('输入q退出游戏：')
    if tips == 'q':
        break