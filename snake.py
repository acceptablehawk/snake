" SNAKE GAME "
import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800,800))

# Constants
GREEN = (0,255,0)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

# Variables
clock = pygame.time.Clock()
x = 250
y = 250
a = random.randint(10,790)
b = random.randint(10,790)
eaten = False
velocity = [0,1]
font = pygame.font.SysFont(None, 36)
snake = []
grade = 0 
counter = 1

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            break
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity[0] = -2
                velocity[1] = 0
                
            if event.key == pygame.K_UP:
                velocity[1] = -2
                velocity[0] = 0
                
            if event.key == pygame.K_RIGHT:
                velocity[0] = 2
                velocity[1] = 0
                
            if event.key == pygame.K_DOWN:
                velocity[1] = 2
                velocity[0] = 0
                
    if x >= 800 or y >= 800 or x <=0 or y <= 0: break

    x += velocity[0]
    y += velocity[1]        

    if eaten:
        snake.append(snake[-1])
        eaten = False
        counter += 1
    else: 
        if len(snake) > counter: snake.pop()
      
    player = pygame.Rect((x,y), (10,10))
    snake.append(player)

    pygame.draw.rect(screen,RED,pygame.Rect((a,b), (10,10)))
    food = pygame.Rect((a,b), (10,10))

    # Drawings    
    if len(snake) != 0:
        for pos in range(len(snake) - 1): 
            snake[pos] = snake[pos+1]
            pygame.draw.rect(screen,GREEN,snake[pos])
            
    score = font.render('Your Score: ' + str(grade), True, BLUE)
    scorerect = score.get_rect()
    scorerect.center = (20, 30)
    screen.blit(score,scorerect)

    
    if player.colliderect(food) == True:
        a = random.randint(10,790)
        b = random.randint(10,790)
        eaten = True
        grade += 1
        
    clock.tick(60)

    pygame.display.flip()
    
    screen.fill(BLACK)
    
while True: 
    gameover = font.render('GAME OVER', True, RED)
    gameoverect = gameover.get_rect()
    gameoverect.center = (400, 400)
    screen.blit(gameover, gameoverect)
    pygame.display.flip()
    
    
    
    
    
    