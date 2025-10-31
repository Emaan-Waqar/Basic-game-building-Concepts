# Write a program to create a Pygame window with a rectangle in it. Keep the background colour as - black RGB(0,0,0) and color of the rectangle as blue (0, 125, 255). Position the rectangle anywhere on the screen. Try changing the values of top, left, height and width to see how the position and size of the rectangle changes.
import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Drawing a rectangle")

b=(0,125,255)
bgColor=(0,0,0)
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
    screen.fill(bgColor)
    pygame.draw.rect(screen,b,pygame.Rect(150,200,250,200),0)
    pygame.draw.rect(screen,b,pygame.Rect(450,200,250,200),1)
    pygame.display.flip()
