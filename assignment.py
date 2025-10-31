import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Drawing two rectangles")
clock=pygame.time.Clock()
class Player(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.image=pygame.Surface((50,50))
        self.image.fill((223, 194, 242))
        self.rect=self.image.get_rect(center=(250,250))
        self.speed=2
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x-=self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x+=self.speed
        if keys[pygame.K_UP]:
            self.rect.y-=self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y+=self.speed
player=Player()
all_sprites=pygame.sprite.Group(player)
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    all_sprites.update()  
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    pygame.draw.rect(screen,(223, 194, 242),pygame.Rect(200,200,50,50),1)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
