import pygame

WIGHT = 600
HEIGHT = 600
SCREEN = (WIGHT, HEIGHT)
FPS = 60

pygame.init()
pygame.display.set_caption("Key event example 1")
screen = pygame.display.set_mode(SCREEN)
clock = pygame.time.Clock()


def move_up(rect: pygame.Rect, s: int):
    rect.centery -= s
    return rect


def move_down(rect: pygame.Rect, s: int):
    rect.centery += s
    return rect


def move_left(rect: pygame.Rect, s: int):
    rect.centerx -= s
    return rect


def move_right(rect: pygame.Rect, s: int):
    rect.centerx += s
    return rect


c = pygame.draw.circle(screen, "forestgreen", (WIGHT / 2, HEIGHT / 2), 10)

running = True
speed = 1
direction = {
    pygame.K_UP: [False, move_up],
    pygame.K_DOWN: [False, move_down],
    pygame.K_LEFT: [False, move_left],
    pygame.K_RIGHT: [False, move_right],
}

while running:
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in direction:
                direction[event.key][0] = True
        elif event.type == pygame.KEYUP:
            if event.key in direction:
                direction[event.key][0] = False

    # Increase speed by 0.1 when any arrow key pressed, max speed equals 10
    if True in tuple(map(lambda x: True in x, direction.values())):
        print(speed)
        speed += 0.1
        if speed > 10:
            speed = 10
    else:
        speed = 1

    # Move circle
    for key, value in direction.items():
        if direction[key][0]:
            c = direction[key][1](c, speed)

    clock.tick(FPS)
    pygame.draw.circle(screen, "forestgreen", (c.centerx, c.centery), 10)
    pygame.display.update()

pygame.quit()
