import pygame

HEIGHT = 600
WIDTH = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True

figures = list()
start_pos = tuple()
rect = pygame.Rect(0, 0, 0, 0)

while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            start_pos = event.pos
            button_pressed = True
        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            rect.width = abs(event.pos[0] - start_pos[0])
            rect.height = abs(event.pos[1] - start_pos[1])
            rect.x = start_pos[0] if start_pos[0] < event.pos[0] else event.pos[0]
            rect.y = start_pos[1] if start_pos[1] < event.pos[1] else event.pos[1]
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if rect.width and rect.height:
                figures.append(rect.copy())
            rect = pygame.Rect(0, 0, 0, 0)

    if pygame.mouse.get_pressed()[2]:
        start_pos = pygame.mouse.get_pos()
        rect.width = 0
        rect.height = 0
    if pygame.mouse.get_pressed()[0]:
        pygame.draw.rect(screen, 'yellow', rect)
    for r in figures:
        pygame.draw.rect(screen, 'yellow', r, width=1)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
