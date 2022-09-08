"""
Draw angry smile
"""

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
pygame.draw.polygon(screen, (0, 0, 0), points=((150, 170), (160, 160), (240, 240), (250, 250)))
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
