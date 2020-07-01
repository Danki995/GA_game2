# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import math
import pygame.mixer

SCREEN = Rect(0, 0, 450, 450)




class niwatori():
    def __init__(self, filename, x, y, score):
        self.imge = pygame.image.load(filename).convert()
        self.rect = self.imge.get_rect()
        self.rect.center = (x, y)
        #self.Flag = Flag
        self.score = score
        print(self.rect)
        # (self.x, self.y) = (x, y)

    def draw(self, screen):
        # self.rect.center(self.x,self.y)
        screen.blit(self.imge, self.rect)

    def move(self):
        self.rect.clamp_ip(SCREEN)




# スプライトのクラス
class Car(pygame.sprite.Sprite):
    # スプライトを作成(画像ファイル名, 位置xy(x, y), 速さvxy(vx, vy), score)
    def __init__(self, filename, xy, vxy, Niwatori, score):
        x, y = xy
        vx, vy = vxy
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        w = self.image.get_width()
        h = self.image.get_height()
        self.rect = Rect(x, y, w, h)
        self.vx = vx
        self.vy = vy
        self.Niwatori = Niwatori
        self.score = score
        #self.hit = 0  # 衝突した回数

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        if self.rect.left < 0:
            self.rect[0] = 425
        if self.rect.top < 0 or self.rect.bottom > SCREEN.height:
            self.vy = -self.vy
        # 壁と衝突時の処理(壁を超えないように)
        self.rect = self.rect.clamp(SCREEN)
        if self.rect.colliderect(self.Niwatori.rect):
            self.score.add_score(-10000)
            self.Niwatori.rect.move_ip(0,50)
class flag():
    def __init__(self, filename, x, y):
        self.imge = pygame.image.load(filename).convert()
        self.rect = self.imge.get_rect()
        self.rect.center = (x, y)
        print(self.rect)
    def draw(self, screen):
        # self.rect.center(self.x,self.y)
        screen.blit(self.imge, self.rect)

class Score():
    def __init__(self, x, y):
        self.sysfont = pygame.font.SysFont(None, 20)
        self.score = 0
        (self.x, self.y) = (x, y)

    def draw(self, screen):
        img = self.sysfont.render("SCORE:" + str(self.score), True, (255, 255, 250))
        screen.blit(img, (self.x, self.y))

    def add_score(self, x):
        self.score += x


def main():
    pygame.init()  # pygame初期化
    screen = pygame.display.set_mode(SCREEN.size)
    score = Score(10,10)
    Flag = flag("flag.png", 225, 25)
    Niwatori = niwatori("niwatori.png", 225, 425, score)
    enemy1 = Car("car.png", (425, 355), (-10, 0), Niwatori, score)
    enemy5 = Car("car.png", (225, 355), (-10, 0), Niwatori, score)
    enemy2 = Car("car.png", (425, 255), (-10, 0), Niwatori, score)
    enemy6 = Car("car.png", (125, 255), (-10, 0), Niwatori, score)
    enemy3 = Car("car.png", (425, 155), (-10, 0), Niwatori, score)
    enemy7 = Car("car.png", (325, 155), (-10, 0), Niwatori, score)
    enemy4 = Car("car.png", (425, 55), (-10, 0), Niwatori, score)
    enemy8 = Car("car.png", (225, 55), (-10, 0), Niwatori, score)
    # スプライトグループの作成
    group = pygame.sprite.RenderUpdates()
    # スプライトの追加
    group.add(enemy1)
    group.add(enemy2)
    group.add(enemy3)
    group.add(enemy4)
    group.add(enemy5)
    group.add(enemy6)
    group.add(enemy7)
    group.add(enemy8)
    #score = Score(10, 10)
    clock = pygame.time.Clock()
    #Niwatori = niwatori("niwatori.png", 225, 425)

    while (1):
        clock.tick(30)  # フレームレート
        screen.fill((0, 20, 0))
        # スプライトグループを更新(キャラクタ3体を一括して更新)
        group.update()
        Flag.draw(screen)
        Niwatori.draw(screen)
        #Flag.draw(screen)
        # スプライトを描画
        group.draw(screen)
        pygame.time.wait(30)  # 更新時間間隔
        for i in range(1, 10):
            pygame.draw.line(screen, (0, 95, 0), (0, 50 * i), (450, 50 * i), 5)  # 直線の描画
            pygame.draw.line(screen, (0, 95, 0), (50 * i, 0), (50 * i, 450), 5)
        score.draw(screen)
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
                    Niwatori.rect.move_ip(-50, 0)
                if event.key == K_RIGHT:
                    Niwatori.rect.move_ip(50, 0)
                if event.key == K_UP:
                    Niwatori.rect.move_ip(0, -50)
                    #print(Niwatori.rect.top)
                if event.key == K_DOWN:
                    Niwatori.rect.move_ip(0, 50)
            if Niwatori.rect.top < 0:
                score.add_score(1000)
                Niwatori.rect.top = 404


if __name__ == "__main__":
    main()