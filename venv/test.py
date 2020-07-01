# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

def main():
    (w,h) = (450,450)   # 画面サイズ
    (x,y) = (w/2, h/2)
    pygame.init()       # pygame初期化
    pygame.display.set_mode((w, h), 0, 32)  # 画面設定
    screen = pygame.display.get_surface()
    im = pygame.image.load("niwatori.png").convert_alpha()
    rect = im.get_rect()
    rect.center = (225, 425)

    while (1):
        pygame.display.update()     # 画面更新
        pygame.time.wait(30)        # 更新時間間隔
        screen.fill((0, 20, 0, 0))  # 画面の背景色
        for i in range(1,10):
            pygame.draw.line(screen, (0, 95, 0), (0, 50*i), (450, 50*i), 5)  # 直線の描画
            pygame.draw.line(screen, (0, 95, 0), (50 * i, 0), (50*i,450 ), 5)
        #pygame.draw.line(screen, (0, 95, 0), (0, 50), (400, 50), 5)  # 直線の描画
        screen.blit(im, rect)       # 画像の描画
        # イベント処理
        for event in pygame.event.get():
            # 画面の閉じるボタンを押したとき
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # キーを押したとき
            if event.type == KEYDOWN:
                # ESCキーなら終了
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # 矢印キーなら円の中心座標を矢印の方向に移動
                if event.key == K_LEFT:
                    rect.move_ip(-50, 0)
                if event.key == K_RIGHT:
                    rect.move_ip(50, 0)
                if event.key == K_UP:
                    rect.move_ip(0, -50)
                if event.key == K_DOWN:
                    rect.move_ip(0, 50)


if __name__ == "__main__":
    main()