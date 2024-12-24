import pygame

pygame.init()
size = width, height = 600, 95
screen = pygame.display.set_mode(size)

car_image = pygame.image.load('data/car2.png').convert_alpha()


class Car(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 5
        self.direction = 1

    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.right >= width or self.rect.left <= 0:
            self.direction *= -1
            self.image = pygame.transform.flip(self.image, True, False)


car = Car(car_image)
all_sprites = pygame.sprite.Group()
all_sprites.add(car)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(50)

pygame.quit()