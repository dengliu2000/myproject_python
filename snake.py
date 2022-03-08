#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 18:26:35 2022

@author: syney
"""

import random
import sys
import time
import pygame
from pygame.locals import *
from collections import deque

SCREEN_WIDTH = 440
SCREEN_HEIGHT = 360
SIZE =20


def print_text(screen, font, x, y, text, fcolor=(255, 255, 255)):
    imgText = font.render(text, True, fcolor)
    screen.blit(imgText, (x, y))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("貪食蛇不再貪食")

    dark = (200, 200, 200)  # 蛇的顏色
    BLUE = (0, 0, 255)   # 食物顏色(+10)
    YELLOW=(255, 255, 0) #食物顏色(+5)
    GREEN=(0, 153, 51) #食物顏色(+20)
    RED =(255, 0 ,0 ) #毒藥顏色(-10)
    PURPLE=(102, 0, 204) #毒藥顏色(-5)


    font1 = pygame.font.SysFont("SimHei", 24)  # 得分的字體
    font2 = pygame.font.Font(None, 72)  # GAME OVER 的字體
    red = (200, 30, 30)                 # GAME OVER 的字體顏色
    fwidth, fheight = font2.size("GAME OVER")
    line_width = 1                      # 網格線寬度
    black = (0, 0, 0)                   # 網格線顏色
    bgcolor = (40, 40, 60)              # 背景色

    # 方向，起始向右
    pos_x = 1
    pos_y = 0
    # 如果蛇正在向右移動，那麽快速點擊向下向左，由於程序刷新沒那麽快，向下事件會被向左覆蓋掉，導致蛇後退，直接GAME OVER
    # b 變量就是用於防止這種情況的發生
    b = True
    # 範圍
    scope_x = (0, SCREEN_WIDTH // SIZE - 1)
    scope_y = (2, SCREEN_HEIGHT // SIZE - 1)
    # 蛇
    snake = deque()
    # 食物
    food1_x = 0
    food1_y = 0
     # 食物
    food2_x = 0
    food2_y = 0
     # 食物
    food3_x = 0
    food3_y = 0
    # 毒藥
    poison1_x = 0
    poison1_y = 0
    # 毒藥
    poison2_x = 0
    poison2_y = 0

    # 初始化蛇
    def _init_snake():
        nonlocal snake
        snake.clear()
        snake.append((2, scope_y[0]))
        snake.append((1, scope_y[0]))
        snake.append((0, scope_y[0]))

    # 食物
    def _create_food1():
        nonlocal food1_x, food1_y
        food1_x = random.randint(scope_x[0], scope_x[1])
        food1_y = random.randint(scope_y[0], scope_y[1])
        while (food1_x, food1_y) in snake:
            # 為了防止食物出到蛇身上
            food1_x = random.randint(scope_x[0], scope_x[1])
            food1_y = random.randint(scope_y[0], scope_y[1])
    def _create_food2():
        nonlocal food2_x, food2_y
        food2_x = random.randint(scope_x[0], scope_x[1])
        food2_y = random.randint(scope_y[0], scope_y[1])
        while (food2_x, food2_y) in snake:
            # 為了防止食物出到蛇身上
            food2_x = random.randint(scope_x[0], scope_x[1])
            food2_y = random.randint(scope_y[0], scope_y[1])
    def _create_food3():
        nonlocal food3_x, food3_y
        food3_x = random.randint(scope_x[0], scope_x[1])
        food3_y = random.randint(scope_y[0], scope_y[1])
        while (food3_x, food3_y) in snake:
            # 為了防止食物出到蛇身上
            food3_x = random.randint(scope_x[0], scope_x[1])
            food3_y = random.randint(scope_y[0], scope_y[1])

    def _create_poison1():
        nonlocal poison1_x, poison1_y
        poison1_x = random.randint(scope_x[0], scope_x[1])
        poison1_y = random.randint(scope_y[0], scope_y[1])
        while (poison1_x, poison1_x) in snake:
            # 為了防止毒藥出到蛇身上
            poison1_x = random.randint(scope_x[0], scope_x[1])
            poison1_y = random.randint(scope_y[0], scope_y[1])

    def _create_poison2():
        nonlocal poison2_x, poison2_y
        poison2_x = random.randint(scope_x[0], scope_x[1])
        poison2_y = random.randint(scope_y[0], scope_y[1])
        while (poison2_x, poison2_x) in snake:
            # 為了防止毒藥出到蛇身上
            poison2_x = random.randint(scope_x[0], scope_x[1])
            poison2_y = random.randint(scope_y[0], scope_y[1])

    game_over = True
    start = False       # 是否開始，當start = True，game_over = True 時，才顯示 GAME OVER
    score = 0           # 得分
    orispeed = 0.2      # 原始速度
    speed = orispeed
    last_move_time = None
    pause = False       # 暫停

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if game_over:
                        start = True
                        game_over = False
                        b = True
                        _init_snake()
                        _create_food1()
                        _create_food2()
                        _create_food3()
                        _create_poison1()
                        _create_poison2()
                        pos_x = 1
                        pos_y = 0
                        # 得分
                        score = 0
                        last_move_time = time.time()
                elif event.key == K_SPACE:
                    if not game_over:
                        pause = not pause
                elif event.key in (K_w, K_UP):
                    # 這個判斷是為了防止蛇向上移時按了向下鍵，導致直接 GAME OVER
                    if b and not pos_y:
                        pos_x = 0
                        pos_y = -1
                        b = False
                elif event.key in (K_s, K_DOWN):
                    if b and not pos_y:
                        pos_x = 0
                        pos_y = 1
                        b = False
                elif event.key in (K_a, K_LEFT):
                    if b and not pos_x:
                        pos_x = -1
                        pos_y = 0
                        b = False
                elif event.key in (K_d, K_RIGHT):
                    if b and not pos_x:
                        pos_x = 1
                        pos_y = 0
                        b = False

        # 填充背景色
        screen.fill(bgcolor)
        # 畫網格線 豎線
        for x in range(SIZE, SCREEN_WIDTH, SIZE):
            pygame.draw.line(screen, black, (x, scope_y[0] * SIZE), (x, SCREEN_HEIGHT), line_width)
        # 畫網格線 橫線
        for y in range(scope_y[0] * SIZE, SCREEN_HEIGHT, SIZE):
            pygame.draw.line(screen, black, (0, y), (SCREEN_WIDTH, y), line_width)

        if game_over:
            if start:
                print_text(screen, font2, (SCREEN_WIDTH - fwidth+10)//2, (SCREEN_HEIGHT - fheight+10)//2, "GAME OVER", red)
        else:
            curTime = time.time()
            if curTime - last_move_time > speed:
                if not pause:
                    b = True
                    last_move_time = curTime
                    next_s = (snake[0][0] + pos_x, snake[0][1] + pos_y)
                    if next_s[0] == food1_x and next_s[1] == food1_y:
                        # 吃到了食物
                        _create_food1()
                        snake.appendleft(next_s)
                        snake.appendleft(next_s)
                        score += 10
                        speed = orispeed - 0.03 * (score // 100)
                    if next_s[0] == food2_x and next_s[1] == food2_y:
                        # 吃到了食物
                        _create_food2()
                        score += 5
                        speed = orispeed - 0.03 * (score // 100)
                    if next_s[0] == food3_x and next_s[1] == food3_y:
                        # 吃到了食物
                        _create_food3()
                        snake.appendleft(next_s)
                        snake.appendleft(next_s)
                        snake.appendleft(next_s)
                        score += 20
                        speed = orispeed - 0.03 * (score // 100)
                    if next_s[0] == poison1_x and next_s[1] == poison1_y:
                        # 吃到了毒藥
                        _create_poison1()
                        snake.pop()
                        score -= 10
                        speed = orispeed - 0.03 * (score // 100)
                    if next_s[0] == poison2_x and next_s[1] == poison2_y:
                        # 吃到了毒藥
                        _create_poison2()
                        snake.pop()
                        score -= 5
                        speed = orispeed - 0.03 * (score // 100)
                    else:
                        if scope_x[0] <= next_s[0] <= scope_x[1] and scope_y[0] <= next_s[1] <= scope_y[1] :
                            snake.appendleft(next_s)
                            snake.pop()
                        else:
                            game_over = True
                        if score == 100:
                            game_over = True

        # 畫食物
        if not game_over:
            # 避免 GAME OVER 的時候把 GAME OVER 的字給遮住了
            pygame.draw.rect(screen, BLUE, (food1_x * SIZE, food1_y * SIZE, SIZE, SIZE), 0)
            pygame.draw.rect(screen, YELLOW, (food2_x * SIZE, food2_y * SIZE, SIZE, SIZE), 0)
            pygame.draw.rect(screen, GREEN, (food3_x * SIZE, food3_y * SIZE, SIZE, SIZE), 0)
            pygame.draw.rect(screen, RED, (poison1_x * SIZE, poison1_y * SIZE, SIZE, SIZE), 0)
            pygame.draw.rect(screen, PURPLE, (poison2_x * SIZE, poison2_y * SIZE, SIZE, SIZE), 0)

        # 畫蛇
        for s in snake:
            pygame.draw.rect(screen, dark, (s[0] * SIZE + line_width, s[1] * SIZE + line_width,
                                            SIZE - line_width * 2, SIZE - line_width * 2), 0)

        print_text(screen, font1, 30, 7, f"Speed: {score/100}")
        print_text(screen, font1, 250, 7, f"Score: {score}")

        pygame.display.update()


if __name__ == "__main__":
    main()