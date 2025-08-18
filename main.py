import pygame


WIDTH = 400
HEIGHT = 250
BUTTON_WIDTH = 50
BUTTON_HEIGHT = 50
BLACK = (0,0,0)

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("╰(*°▽°*)╯")

background_image = pygame.image.load('background.jpg')
background_image = pygame.transform.scale(background_image, (WIDTH,HEIGHT))

button_image = pygame.image.load('button_image.jpg')
button_image = pygame.transform.scale(button_image, (BUTTON_WIDTH,BUTTON_HEIGHT))

dark_button_image = pygame.image.load('dark_button_image.png')
dark_button_image = pygame.transform.scale(dark_button_image, (BUTTON_WIDTH,BUTTON_HEIGHT))

buttons = []

for i in range(1, 7):
    x = (i - 1) % 3 * (BUTTON_HEIGHT + 10) + 50
    y = (i - 1) // 3 * (BUTTON_HEIGHT + 10) + 50
    button_rect = pygame.Rect(x,y,BUTTON_WIDTH, BUTTON_HEIGHT)
    buttons.append(button_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, button in enumerate(buttons):
                    if button.collidepoint(event.pos):
                        print("IT WORKS 😂😂😂")

    window.blit(background_image, (0, 0))

    for i, button in enumerate(buttons):
        if button.collidepoint(pygame.mouse.get_pos()):
            window.blit(dark_button_image, button)
        else:
            window.blit(button_image, button)

        font = pygame.font.SysFont(None, 30)
        text = font.render(str(i + 1), True, BLACK)
        text_rect = text.get_rect(center=button.center)
        window.blit(text, text_rect)
    pygame.display.flip()