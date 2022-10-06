import pygame

WIDTH = 600
HEIGHT = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

current_speed = 1.0
MAX_SPEED = 10

figure = pygame.draw.circle(screen, "forestgreen", (WIDTH/2, HEIGHT/2), 10)


def move_up(rect: pygame.Rect, speed: float) -> pygame.Rect:
    rect.centery -= speed
    return rect


def move_down(rect: pygame.Rect, speed: float) -> pygame.Rect:
    rect.centery += speed
    return rect


def move_left(rect: pygame.Rect, speed: float) -> pygame.Rect:
    rect.centerx -= speed
    return rect


def move_right(rect: pygame.Rect, speed: float) -> pygame.Rect:
    rect.centerx += speed
    return rect


direction = {
    pygame.K_UP: move_up,
    pygame.K_DOWN: move_down,
    pygame.K_LEFT: move_left,
    pygame.K_RIGHT: move_right,
}

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    key_down_flag = False
    for key in direction.keys():
        if keys[key]:
            key_down_flag = True
            figure = direction[key](figure, current_speed)
            current_speed += 0.1
            if current_speed > MAX_SPEED:
                current_speed = MAX_SPEED

    if not key_down_flag:
        current_speed = 1

    screen.fill("black")
    pygame.draw.circle(screen, "forestgreen", (figure.centerx, figure.centery), 10)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()