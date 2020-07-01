# -*- coding:utf-8 -*-
import pygame


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
size=(700,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Pygame") #
screen.fill(WHITE)

pygame.draw.rect(screen, RED, [55, 50, 20, 25],1)
pygame.display.update()
pygame.display.flip()
pygame.time.delay(50000) #5000ミリ秒(つまり5秒)待つ

pygame.quit()