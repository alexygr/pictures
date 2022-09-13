"""
Draw angry smile
"""
import math

import pygame

FPS = 30
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Angry smile")
screen.fill((217, 217, 217))

# Draw Face
pygame.draw.circle(screen, (249, 249, 6), center=(300, 300), radius=150)
pygame.draw.circle(screen, (0, 0, 0), center=(300, 300), radius=150, width=2)

# Draw eyes

# Left eye
pygame.draw.circle(screen, (255, 0, 0), center=(230, 270), radius=32)
pygame.draw.circle(screen, (0, 0, 0), center=(230, 270), radius=32, width=2)
pygame.draw.circle(screen, (0, 0, 0), center=(230, 270), radius=13)
# Right eye
pygame.draw.circle(screen, (255, 0, 0), center=(370, 270), radius=25)
pygame.draw.circle(screen, (0, 0, 0), center=(370, 270), radius=25, width=2)
pygame.draw.circle(screen, (0, 0, 0), center=(370, 270), radius=13)


# Draw eyebrow
# Left eyebrow
# Calkulate left brow coordinate
def curve_rect(start_position, length, height, angle=0):
    """
    Calculate rectangle coordinates concerning angle
    :param start_position: Start position of rectangle, left bottom corner
    :param length: length of rectangle
    :param height: height of rectangle
    :param angle: angle of drawing rectangle concerning axis X -90 -> 90
    :return: list of dots
    """
    dots = list()
    dots.append(start_position)
    angle = (360 + angle) % 360
    length_x = math.cos(math.radians(angle)) * length
    length_y = math.sin(math.radians(angle)) * length
    dots.append((start_position[0] + length_x, start_position[1] + length_y))
    height_x = -math.sin(math.radians(angle)) * height
    height_y = math.cos(math.radians(angle)) * height
    dots.append((start_position[0] + length_x + height_x, start_position[1] + length_y + height_y))
    dots.append((start_position[0] + height_x, start_position[1] + height_y))
    print(dots, angle)
    return dots


right_brow = curve_rect(start_position=(150, 230), length=150, height=10, angle=30)
pygame.draw.polygon(screen, (0, 0, 0), right_brow)
# Right brow


pygame.display.update()

clock = pygame.time.Clock()
clock.tick(FPS)
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
