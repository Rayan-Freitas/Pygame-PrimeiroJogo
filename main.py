import pygame 
import random
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Primeiro Jogo")

FPS = 60

VELOCITY = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

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
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(SPACESHIP_P1, (p1.x, p1.y))
    WIN.blit(SPACESHIP_P2, (p2.x, p2.y))
    pygame.display.update()

def p1_movement(keys_pressed, p1):
    if keys_pressed[pygame.K_a] and p1.x - VELOCITY > 0: # Esquerda
        p1.x -= VELOCITY
    if keys_pressed[pygame.K_d] and p1.x + VELOCITY + p1.width < BORDER.x: # Direita
        p1.x += VELOCITY
    if keys_pressed[pygame.K_w] and p1.y - VELOCITY > 0: # Cima
        p1.y -= VELOCITY
    if keys_pressed[pygame.K_s]  and p1.y + VELOCITY + p1.width < HEIGHT - 15: # Baixo e verificação de borda
        p1.y += VELOCITY

def p2_movement(keys_pressed, p2):
    if keys_pressed[pygame.K_LEFT] and p2.x - VELOCITY > BORDER.x + BORDER.width: # Esquerda
        p2.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and p2.x + VELOCITY + p2.width < WIDTH: # Direita
        p2.x += VELOCITY
    if keys_pressed[pygame.K_UP] and p2.y - VELOCITY > 0: # Cima
        p2.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and p2.y + VELOCITY + p2.width < HEIGHT - 15: # Baixo e verificação de borda
        p2.y += VELOCITY

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

        keys_pressed = pygame.key.get_pressed()
        p1_movement(keys_pressed, p1)
        p2_movement(keys_pressed, p2)

        draw_window(p1, p2)

    pygame.quit()


if __name__ == "__main__":
    main()