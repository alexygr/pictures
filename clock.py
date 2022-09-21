import math
import time

import pygame

SCREEN_HEIGHT = 710
SCREEN_WIGHT = 610
SCREEN_HEIGHT_MIDDLE = SCREEN_HEIGHT / 2
SCREEN_WIGHT_MIDDLE = SCREEN_WIGHT / 2
MARGIN = 20
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')

H = 0.6
M = 0.8
S = 0.9

H_ANGLE = 30
M_ANGLE = H_ANGLE / 60
S_ANGLE = 6

FPS = 2

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIGHT, SCREEN_HEIGHT))
pygame.display.set_caption('Clock')

clock = pygame.time.Clock()
running = True


def get_end_pos(tm_sec, length, s=0):
    angle = (S_ANGLE * tm_sec - 90) + (s * M_ANGLE)
    x_length = (SCREEN_WIGHT_MIDDLE - MARGIN) * length
    y_length = (SCREEN_HEIGHT_MIDDLE - MARGIN) * length
    x = math.cos(math.radians(angle)) * x_length + SCREEN_WIGHT_MIDDLE
    y = math.sin(math.radians(angle)) * y_length + SCREEN_HEIGHT_MIDDLE
    print(f"{x=} {y=} {tm_sec=} angle={angle}")
    return x, y


def draw_clock_face():
    pygame.draw.ellipse(screen, WHITE, (MARGIN, MARGIN, SCREEN_WIGHT - MARGIN*2, SCREEN_HEIGHT - MARGIN*2), width=1)
    for sec in range(60):
        if sec % 5 == 0:
            pygame.draw.aaline(screen, WHITE, start_pos=get_end_pos(sec, S * 1.02), end_pos=get_end_pos(sec, 1))
        else:
            pygame.draw.aaline(screen, WHITE, start_pos=get_end_pos(sec, S * 1.05),
                               end_pos=get_end_pos(sec, 1))


while running:
    clock.tick(FPS)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_clock_face()

    t = time.localtime()
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIGHT_MIDDLE, SCREEN_HEIGHT_MIDDLE), end_pos=get_end_pos(t.tm_sec, S))
    pygame.draw.line(screen, WHITE, (SCREEN_WIGHT_MIDDLE, SCREEN_HEIGHT_MIDDLE),
                     end_pos=get_end_pos(t.tm_min, M),
                     width=3)
    pygame.draw.line(screen, WHITE, (SCREEN_WIGHT_MIDDLE, SCREEN_HEIGHT_MIDDLE),
                     end_pos=get_end_pos(t.tm_hour * 5 % 60, H, t.tm_min), width=5)

    pygame.display.update()

pygame.quit()
