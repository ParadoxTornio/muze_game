import pygame

pygame.init()

H = 550
W = 600
window = pygame.display.set_mode((W, H))
labirint = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
start = 50
lines = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, position, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.rect.x += width // 2

    def update(self):
        if self.rect.left > W:
            self.rect.right = 0
        if self.rect.top > H:
            self.rect.bottom = 0
        if self.rect.right < 0:
            self.rect.left = W
        if self.rect.bottom < 0:
            self.rect.top = H


class Labirint(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def print_labirint(self, list_):
        counter_x = 0
        counter_y = 0
        for i in labirint:
            for j in i:
                if j == 1:
                    line = pygame.Surface((20, 20))
                    line_rect = line.get_rect()
                    line_rect.x = start + counter_x
                    line_rect.y = start + counter_y
                counter_x += 20
            counter_y += 20
            counter_x = 0


player = Player((0, H // 2), (0, 0, 0), 20, 20)
labirint_object = Labirint()
players = pygame.sprite.Group()
players.add(player)
lines.add(labirint_object)
clock = pygame.time.Clock()
FPS = 60
game = True
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player.rect.y -= 2.5
    if key[pygame.K_s]:
        player.rect.y += 2.5
    if key[pygame.K_a]:
        player.rect.x -= 2.5
    if key[pygame.K_d]:
        player.rect.x += 2.5
    players.update()
    window.fill((255, 255, 255))
    players.draw(window)
    lines.draw(window)
    labirint_object.print_labirint(labirint)
    pygame.display.flip()

pygame.quit()
# import pygame
#
# pygame.init()
#
# H = 550
# W = 600
# window = pygame.display.set_mode((W, H))
# labirint = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
#             [1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
#             [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
#             [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#             [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
#             [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
#             [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
#             [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
#             [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
#             [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
#             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
# start = 50
#
#
# class Player(pygame.sprite.Sprite):
#     def __init__(self, position, color, width, height):
#         pygame.sprite.Sprite.__init__(self)
#         self.position = position
#         self.image = pygame.Surface((width, height))
#         self.image.fill(color)
#         self.rect = self.image.get_rect()
#         self.rect.center = self.position
#         self.rect.x += width // 2
#
#     def update(self):
#         if self.rect.left > W:
#             self.rect.right = 0
#         if self.rect.top > H:
#             self.rect.bottom = 0
#         if self.rect.right < 0:
#             self.rect.left = W
#         if self.rect.bottom < 0:
#             self.rect.top = H
#
# def print_labirint(self, list_):
#     counter_x = 0
#     counter_y = 0
#     for i in labirint:
#         for j in i:
#             if j == 1:
#                 rect = pygame.draw.rect(window, (100, 100, 100),
#                                         (start + counter_x, start + counter_y,
#                                          20, 20))
#             counter_x += 20
#         counter_y += 20
#         counter_x = 0
#
#
# player = Player((0, H // 2), (0, 0, 0), 20, 20)
# players = pygame.sprite.Group()
# players.add(player)
# clock = pygame.time.Clock()
# FPS = 60
# game = True
# while game:
#     clock.tick(FPS)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game = False
#     key = pygame.key.get_pressed()
#     if key[pygame.K_w]:
#         player.rect.y -= 2.5
#     if key[pygame.K_s]:
#         player.rect.y += 2.5
#     if key[pygame.K_a]:
#         player.rect.x -= 2.5
#     if key[pygame.K_d]:
#         player.rect.x += 2.5
#     players.update()
#     window.fill((255, 255, 255))
#     players.draw(window)
#     player.print_labirint(labirint)
#     pygame.display.flip()
#
# pygame.quit()
