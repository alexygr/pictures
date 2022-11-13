import pygame

HEIGHT = 600
WIDTH = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True

rect_colors = list()
rect_blue = list()
rect_c = 0  # current selected rectangle
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
        if event.type == pygame.MOUSEMOTION and True not in pygame.mouse.get_pressed():
            rect_blue = list()
            rect_c = 0  # current selected rectangle
            for i, r in enumerate(figures):
                if r.collidepoint(event.pos):
                    rect_colors[i] = 'blue'
                    rect_blue.append(i)
                else:
                    rect_colors[i] = 'yellow'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # mouse wheel up
                for i, r in enumerate(rect_blue):  # Set color Yellow to all rectangle except one
                    if i != rect_c:
                        rect_colors[r] = 'yellow'
                    else:
                        rect_colors[r] = 'blue'
                rect_c = rect_c + 1
                if rect_c > i:
                    rect_c = 0
            elif event.button == 5:  # mouse wheel down
                for i, r in enumerate(rect_blue):  # Set color Yellow to all rectangle except one
                    if i != rect_c:
                        rect_colors[r] = 'yellow'
                    else:
                        rect_colors[r] = 'blue'
                rect_c = rect_c - 1
                if rect_c < 0:
                    rect_c = i
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if rect.width and rect.height:
                figures.append(rect.copy())
                rect_colors.append("yellow")
            rect = pygame.Rect(0, 0, 0, 0)

    if pygame.mouse.get_pressed()[2] and pygame.mouse.get_pressed()[0]:
        start_pos = pygame.mouse.get_pos()
        rect.width = 0
        rect.height = 0

    if pygame.mouse.get_pressed()[0]:
        pygame.draw.rect(screen, 'yellow', rect, width=1)
    for i, r in enumerate(figures):
        pygame.draw.rect(screen, rect_colors[i], r, width=1)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
