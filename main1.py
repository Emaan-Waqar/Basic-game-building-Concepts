# Write a program to create a Pygame window with two circles, one solid and another hollow circle with border width 3. Keep the background colour as - white RGB(255, 255, 255) and the colour of the rectangle as green (0, 255, 0). Try changing the values of centre and radius to see how the position and size of the balls change.
import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Drawing a rectangle")

green=(0,255,0)
white=(255,255,255)
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
    screen.fill(white)
    pygame.draw.circle(screen,green,(200,200),50,3)
    pygame.draw.circle(screen,green,(400,400),50,0)
    pygame.display.flip()
