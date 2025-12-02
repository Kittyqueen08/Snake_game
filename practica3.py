import pygame 
import random
pygame.init()

WIDTH=600
HEIGHT=400
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake")

BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
WHITE=(255,255,255)

block=20

clock=pygame.time.Clock()
snake_speed=10

def draw_snake(snake_list):
    for x,y in snake_list:
        pygame.draw.rect(win,GREEN,(x,y,block,block))

def game_loop():
    game_over= False
    game_close=False

    x= WIDTH//2
    y=HEIGHT//2

    dx=0
    dy=0
    snake_list=[]
    length=1

    food_x=random.randrange(0,WIDTH-block,block)
    food_y=random.randrange(0,HEIGHT-block,block)
    
    font=pygame.font.SysFont(None,35)
    while not game_over:
        while game_close:
            win.fill(BLACK)
            msg=font.render("Game Over, presiona la tecla e para salir",True,WHITE)
            win.blit(msg,(WIDTH/4,HEIGHT/3))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_e:
                        game_over=True
                        game_close=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over= True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and dx==0:
                    dx=-block
                    dy=0
                elif event.key==pygame.K_RIGHT and dx==0:
                    dx=block
                    dy=0
                elif event.key==pygame.K_UP and dy==0:
                    dx=0
                    dy=-block
                elif event.key==pygame.K_DOWN and dy==0:
                    dx=0
                    dy=block
    

        x+=dx
        y+=dy

        if x<0 or x>=WIDTH or y <0 or y>=HEIGHT:
            game_close=True
        win.fill(BLACK)

        pygame.draw.rect(win,RED,(food_x,food_y,block,block))

        snake_head =[x,y]
        snake_list.append(snake_head)
        if len(snake_list)>length:
            del snake_list[0]
        
        for part in snake_list[:-1]:
            if part==snake_head:
                game_close=True
        
        draw_snake(snake_list)
        pygame.display.update()
        if x==food_x and y==food_y:
            food_x=random.randrange(0,WIDTH-block,block)
            food_y=random.randrange(0,HEIGHT-block,block)
            length+=1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
     
game_loop