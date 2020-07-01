# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import math
import pygame.mixer


SCREEN = Rect(0, 0, 450, 450)
# スプライトのクラス
class Car(pygame.sprite.Sprite):
    # スプライトを作成(画像ファイル名, 位置xy(x, y), 速さvxy(vx, vy), 回転angle)
    def __init__(self, filename, xy, vxy, angle=0):
        x, y = xy
        vx, vy = vxy
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        if angle != 0: self.image = pygame.transform.rotate(self.image, angle)
        w = self.image.get_width()
        h = self.image.get_height()
        self.rect = Rect(x, y, w, h)
        #print(self.rect[0])
        self.vx = vx
        #print(self.vx)
        self.vy = vy
        self.angle = angle

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        # 壁と衝突時の処理(跳ね返り)
        #if self.rect.left < 0 or self.rect.right > SCREEN.width:
            #self.vx = -self.vx
        if self.rect.left < 0:
            self.rect[0]=425
        if self.rect.top < 0 or self.rect.bottom > SCREEN.height:
            self.vy = -self.vy
        # 壁と衝突時の処理(壁を超えないように)
        self.rect = self.rect.clamp(SCREEN)

class Score():
    def __init__(self, x, y):
        self.sysfont = pygame.font.SysFont(None, 20)
        self.score = 0
        (self.x, self.y) = (x, y)
    def draw(self, screen):
        img = self.sysfont.render("SCORE:"+str(self.score), True, (255,255,250))
        screen.blit(img, (self.x, self.y))
    def add_score(self, x):
        self.score += x




def main():
    pygame.init()       # pygame初期化
    screen = pygame.display.set_mode(SCREEN.size)
    im = pygame.image.load("niwatori.png").convert_alpha()
    enemy1 = Car("car.png", (425,355),(-20,0),0)
    enemy2 = Car("car.png", (425,255),(-20,0),0)
    enemy3 = Car("car.png", (425,155),(-20,0),0)
    enemy4 = Car("car.png", (425,55),(-20,0),0)
    # スプライトグループの作成
    group = pygame.sprite.RenderUpdates()
    # スプライトの追加
    group.add(enemy1)
    group.add(enemy2)
    group.add(enemy3)
    group.add(enemy4)
    score = Score(10,10)
    clock = pygame.time.Clock()
    rect = im.get_rect()
    rect.center = (225, 425)

    while (1):
        clock.tick(30) #フレームレート
        screen.fill((0, 20, 0))
        # スプライトグループを更新(キャラクタ3体を一括して更新)
        group.update()

        # スプライトを描画
        group.draw(screen)
        pygame.time.wait(30)        # 更新時間間隔
        for i in range(1,10):
            pygame.draw.line(screen, (0, 95, 0), (0, 50*i), (450, 50*i), 5)  # 直線の描画
            pygame.draw.line(screen, (0, 95, 0), (50 * i, 0), (50*i,450 ), 5)
        screen.blit(im, rect)       # 画像の描画
        pygame.display.update()  # 画面更新
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