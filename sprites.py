import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        #  methods are required for pygame.sprite.Group
        self.image  = pygame.image.load("birdpic.png")

        self.rect   = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #  constants
        self.JUMP       = 5
        self.GRAVITY    = 0.4
        self.WIDTH      = 30
        self.HEIGHT     = 30
        self.MOVE_SPEED = 0
        #  allows class Bird to use methods of pygame.sprite.Sprite
        #  equal to pygame.sprite.Sprite.__init__(self)
        super().__init__()

    def move(self, up):
        if up:
            self.MOVE_SPEED = -self.JUMP

        self.MOVE_SPEED += self.GRAVITY
        self.rect.y += self.MOVE_SPEED


class Tube(pygame.sprite.Sprite):
    def __init__(self, x, y, height):
        #  constants
        self.PLATFORM_SPEED  = 3
        self.PLATFORM_WIDTH  = 100
        self.PLATFORM_HEIGHT = height
        self.COLOR           = "#008800"

        self.image  = pygame.Surface((self.PLATFORM_WIDTH, self.PLATFORM_HEIGHT))
        self.image.fill(pygame.Color(self.COLOR))

        self.rect   = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        super().__init__()

    def move(self):
        self.rect.x -= self.PLATFORM_SPEED
