import pygame, random, sprites
from pygame.locals import *


SCREEN_SIZE = 800, 640
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    timer = pygame.time.Clock()

    bg = pygame.image.load("bg.jpg")
    bird = sprites.Bird(100, 100)
    #  ============= TUBE GENERATION =============
    #  Tube constants
    TUBE_GAP = 150
    TUBE_UNDERGROUND = 50
    DISTANCE = 350

    def make_and_add_tube(group):
        START_POSITION = 0
        if group.sprites():
            START_POSITION = max([sprite.rect.x for sprite in group.sprites()])

        TOP_TUBE_HEIGHT   = random.randint(40, 450) + TUBE_UNDERGROUND
        TOP_TUBE_POSITION = -TUBE_UNDERGROUND
        BOT_TUBE_POSITION = (TOP_TUBE_HEIGHT - TUBE_UNDERGROUND) + TUBE_GAP
        BOT_TUBE_HEIGHT   = 640 - BOT_TUBE_POSITION + TUBE_UNDERGROUND

        pf_top = sprites.Tube(START_POSITION + DISTANCE, TOP_TUBE_POSITION, TOP_TUBE_HEIGHT)
        pf_bot = sprites.Tube(START_POSITION + DISTANCE, BOT_TUBE_POSITION, BOT_TUBE_HEIGHT)

        group.add(pf_top, pf_bot)

    all_sprites = pygame.sprite.Group()
    hero = pygame.sprite.Group()
    hero.add(bird)

    for i in range(3):
        make_and_add_tube(all_sprites)

    game = True
    up = False

    while game:
        timer.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                game = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   game = False
                if event.key == K_UP:
                    up = True

            if event.type == KEYUP:
                if event.key == K_UP:
                    up = False

        ass = all_sprites.sprites()
        black_list = []
        for tube in range(len(ass)):
            if ass[tube].rect.x < -ass[tube].PLATFORM_WIDTH:
                black_list.append(ass[tube])
                make_and_add_tube(all_sprites)
                all_sprites.remove(black_list)
                black_list.clear()
        screen.blit(bg, (0,0))
        for i in all_sprites:
            i.move()
        bird.move(up)
        hero.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
