import pygame
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("My first game screen")
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(125,125,125),pygame.Rect(200,120,250,250),0)
    pygame.display.flip()
