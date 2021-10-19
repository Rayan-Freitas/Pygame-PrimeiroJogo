import pygame 
import random
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Primeiro Jogo")

FPS = 60

WHITE = (255, 255, 255)

SPACESHIP_HEIGHT, SPACESHIP_WIDTH = 55, 40

SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship.png'))
SPACESHIP_P1 = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_IMAGE, (SPACESHIP_HEIGHT, SPACESHIP_WIDTH)), 270)
SPACESHIP_P2 = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_IMAGE, (SPACESHIP_HEIGHT, SPACESHIP_WIDTH)), 90)

SPACESHIP_HEIGHT, SPACESHIP_WIDTH = 55, 40

LASER_IMAGE = pygame.image.load(os.path.join('Assets', 'laser.png'))
SPACE_BACKGROUND = pygame.image.load(os.path.join('Assets', 'spacebg.gif'))
SPACE_BACKGROUND2 = pygame.image.load(os.path.join('Assets', 'spacebg2.gif'))

#def draw_window(a):
#    WIN.fill(a)
#    pygame.display.update()

def draw_window(p1, p2):
    WIN.fill(WHITE)
    WIN.blit(SPACESHIP_P1, (p1.x, p1.y))
    WIN.blit(SPACESHIP_P2, (p2.x, p2.y))
    pygame.display.update()

def main():
    p1 = pygame.Rect(100, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    p2 = pygame.Rect(700, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #RANDOM_NUMBER = random.randint(0,255)
        #random_N = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        p1.x += 1
        draw_window(p1, p2)

    pygame.quit()


if __name__ == "__main__":
    main()