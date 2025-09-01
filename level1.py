from settings import *
def level1():
    import pygame

    from player import Player
    from game_objects import Portal, Trap, Coin, Food, Platform

    platforms = []
    platforms.append(Platform(0, 100, 100, 50))
    platforms.append(Platform(150, 100, 100, 50))

    portal = Portal(400, 300)

    coins = []
    coins.append(Coin(170, 70))

    player = Player(50, 50)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            player.move_right()
        if keys[pygame.K_a]:
            player.move_left()
        player.update_hitbox()
        player.vertical_motion()

        for platform in platforms:
            if player.platform_collision(platform):
                break

        screen.fill((255, 255, 255))
        screen.blit(player.image, player.hitbox)
        for platform in platforms:
            screen.blit(platform.image, platform.hitbox)
        for coin in coins:
            screen.blit(coin.image, coin.hitbox)
        screen.blit(portal.image, portal.hitbox)
        pygame.display.flip()
        pygame.time.Clock().tick(60)