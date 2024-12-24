import pygame
import random

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)

bomb = pygame.image.load('data/bomb.png')
boom = pygame.image.load('data/boom.png')
bomb_size = bomb.get_rect().size


class Bomb:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, *bomb_size)
        self.image = bomb

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def boom(self):
        self.image = boom

def place_bombs():
    bombs = []
    for _ in range(20):
        x = random.randint(0, width - bomb_size[0])
        y = random.randint(0, height - bomb_size[1])
        bombs.append(Bomb(x, y))
    return bombs

bombs = place_bombs()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for bomb in bombs:
                if bomb.rect.collidepoint(pos):
                    bomb.boom()

    screen.fill((0, 0, 0))

    for bomb in bombs:
        bomb.draw(screen)

    pygame.display.flip()
pygame.quit()