import pygame 
import random
import os
pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Primeiro Jogo")

FPS = 60
VELOCITY = 3
BULLETS_VEL = 7
MAX_BULLETS = 

P1_HIT = pygame.USEREVENT + 1
P2_HIT = pygame.USEREVENT + 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

SPACESHIP_HEIGHT, SPACESHIP_WIDTH = 55, 40

SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship.png'))
SPACESHIP_P1 = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_IMAGE, (SPACESHIP_HEIGHT, SPACESHIP_WIDTH)), 270)
SPACESHIP_P2 = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_IMAGE, (SPACESHIP_HEIGHT, SPACESHIP_WIDTH)), 90)



SPACESHIP_HEIGHT, SPACESHIP_WIDTH = 55, 40

LASER_IMAGE = pygame.image.load(os.path.join('Assets', 'laser.png'))
SPACE_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'spacebg.gif')), (WIDTH, HEIGHT))
SPACE_BACKGROUND2 = pygame.image.load(os.path.join('Assets', 'spacebg2.gif'))

#def draw_window(a):
#    WIN.fill(a)
#    pygame.display.update()

def draw_window(p1, p2, p2_bullets, p1_bullets, p2_health, p1_health):
    WIN.blit(SPACE_BACKGROUND, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    p2_health_text = HEALTH_FONT.render("Health: " + str(p2_health), 1, WHITE)
    p1_health_text = HEALTH_FONT.render("Health: " + str(p1_health), 1, WHITE)
    WIN.blit(p2_health_text, (WIDTH - p2_health_text.get_width() - 10, 10))
    WIN.blit(p1_health_text, (10, 10))


    WIN.blit(SPACESHIP_P1, (p1.x, p1.y))
    WIN.blit(SPACESHIP_P2, (p2.x, p2.y))

    for bullet in p2_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in p1_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

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

def handle_bullets(p1_bullets, p2_bullets, p1, p2):
    for bullet in p1_bullets:
        bullet.x += BULLETS_VEL
        if p2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(P2_HIT))
            p1_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            p1_bullets.remove(bullet)

    for bullet in p1_bullets:
        bullet.x -= BULLETS_VEL
        if p2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(P1_HIT))
            p1_bullets.remove(bullet)
        elif bullet.x < 0:
            p1_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

    
p1_bullets = []
p2_bullets = []

p1_health = 10
p2_health = 10

def main():
    p1 = pygame.Rect(100, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    p2 = pygame.Rect(700, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(p1_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(p1.x + p1.width, p1.y + p1.height//2 - 2, 10, 5)
                    p1_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(p2_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(p2.x + p2.y, + p2.height//2 - 2, 10, 5)
                    p2_bullets.append(bullet)

            if event.type == P2_HIT:
                p2_health -= 1


            if event.type == P1_HIT
                p1_health -= 1


        winner_text = ""
        if p1_health <= 0:
            winner_text = "P1 Wins!"

        if p2_health <= 0: 
            winner_text = "P2 Wins!"

        if winner_text != ""
            draw_winner(winner_text)
            break

        #RANDOM_NUMBER = random.randint(0,255)
        #random_N = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        #print(p1_bullets, p2_bullets)  debug bullets
        keys_pressed = pygame.key.get_pressed()
        p1_movement(keys_pressed, p1)
        p2_movement(keys_pressed, p2)


        handle_bullets(p1_bullets, p2_bullets, p1, p2)

        draw_window(p1, p2, p2_bullets, p1_bullets, p2_health, p1_health)

    main()


if __name__ == "__main__":
    main()