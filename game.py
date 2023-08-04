import pygame
from settings import *
from sprites import Player, MuzeCell, EndGame


class Game:
    def __init__(self, p):
        # initialize game window, etc
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.player = p
        self.end_surface = EndGame()
        self.end_surface_rect = self.end_surface.rect
        self.players_sprites = pygame.sprite.Group()
        self.muze_sprites = pygame.sprite.Group()
        self.end_sprites = pygame.sprite.Group()
        self.running = True

    def new(self):
        # start a new game
        self.players_sprites.add(self.player)
        self.end_sprites.add(self.end_surface)
        self.create_muze(labirint)
        self.run()

    def run(self):
        # Game Loop
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.players_sprites.update()
        self.muze_sprites.update()
        if pygame.sprite.groupcollide(self.players_sprites, self.muze_sprites, False, False):
            self.running = False
        if pygame.sprite.groupcollide(self.players_sprites, self.end_sprites, False, False):
            self.running = False
            self.show_end_screen()

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                self.running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                player.rect.y -= 2
            elif key[pygame.K_s]:
                player.rect.y += 2
            elif key[pygame.K_a]:
                player.rect.x -= 2
            elif key[pygame.K_d]:
                player.rect.x += 2

    def draw(self):
        # Game Loop - draw
        self.screen.fill(WHITE)
        self.players_sprites.draw(self.screen)
        self.muze_sprites.draw(self.screen)
        self.end_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_end_screen(self):
        self.screen.fill((0, 128, 0))
        sys_font = pygame.font.SysFont('Arial', 75, False, False)
        text_surface = sys_font.render('YOU WIN!!!', True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 3)
        self.screen.blit(text_surface, text_rect)
        sys_font_2 = pygame.font.SysFont('Arial', 50, False, False)
        text_surface_2 = sys_font_2.render('Exit-->q     Continue-->c', True, (255, 255, 255))
        text_rect_2 = text_surface_2.get_rect()
        text_rect_2.center = (WIDTH // 2, HEIGHT // 3 + 100)
        self.screen.blit(text_surface_2, text_rect_2)
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if key[pygame.K_q]:
                    waiting = False
                    self.running = False
                elif key[pygame.K_c]:
                    waiting = False
                    self.running = True
                    self.player.reset_position()
                    self.new()

    def show_continue_screen(self):
        # game over/continue
        self.screen.fill((0, 0, 0))
        sys_font = pygame.font.SysFont('Arial', 50, False, False)
        text_surface = sys_font.render('Exit-->q     Continue-->c', True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 3)
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if key[pygame.K_q]:
                    waiting = False
                    self.running = False
                elif key[pygame.K_c]:
                    waiting = False
                    self.running = True
                    self.player.reset_position()
                    self.new()

    def create_muze(self, list_):
        counter_x = 0
        counter_y = 0
        for i in list_:
            for j in i:
                if j == 1:
                    pixel = MuzeCell((start + counter_x, counter_y + 10))
                    pixel2 = MuzeCell((start + counter_x + 10, counter_y + 10))
                    self.muze_sprites.add(pixel)
                    self.muze_sprites.add(pixel2)
                counter_x += 20
            counter_y += 20
            counter_x = 0


player = Player((0, 29.5), (0, 0, 0), 15, 11)
g = Game(player)
g.show_start_screen()
while g.running:
    g.new()
    g.show_continue_screen()

pygame.quit()
