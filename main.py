import pygame
import random

#Definir une clock (util pour fps)
clock = pygame.time.Clock()
FPS = 30

#Class Ball
class Ball(pygame.sprite.Sprite) :
    def __init__(self,x,y,weight,height):
        self.x = x
        self.y = y
        self.height = int(height)
        self.weight = weight
        self.velocity = [random.randint(4,7),random.randint(-8,8)]
        self.rect = pygame.Rect(x,y,weight,height)
    def afficher(self,screen) :
        pygame.draw.rect(screen,white,self.rect)
    def move(self,velocity) :
        self.rect.y += velocity[1]
        self.rect.x += velocity[0]
    def rebond_pallet(self) :
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(-4,4)
        self.rect.y += self.velocity[1]
        self.rect.x += self.velocity[0]

#Class Player
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,weight,height) : 
        self.x = x
        self.y = y
        self.height = int(height)
        self.player_rect = pygame.Rect(x,y,weight,height)
    def move(self,vitesse):
        self.player_rect.y += vitesse
        if self.player_rect.y < 0 or self.player_rect.y + self.height > 500 :
            self.player_rect.y -= vitesse
    def afficher(self,screen):
        pygame.draw.rect(screen,white,self.player_rect)


#Color
white = (255,255,255)
black = (0,0,0)
#----#

pygame.init()
screen = pygame.display.set_mode((900,500))
pygame.display.set_caption("Beta of Pong")

#Player making
Player1 = Player(20,210,20,80)
Player2 = Player(860,210,20,80)
#----#

#Balle making
ball = Ball(450,210,20,20)
#----#



player1_vitesse = 0
player2_vitesse = 0
Score_Player1 = 0
Score_PLayer2 = 0
start = False
game = True
tour = 1
while game:
    if tour%3 == 0 :
        tour = 1
        FPS += 5
        print(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP :
                player2_vitesse = -7
            if event.key == pygame.K_DOWN :
                player2_vitesse = 7
            if event.key == pygame.K_a :
                player1_vitesse = -7
            if event.key == pygame.K_q :
                player1_vitesse = 7
            if event.key == pygame.K_SPACE:
                start = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP :
                player2_vitesse = 0
            if event.key == pygame.K_DOWN :
                player2_vitesse = 0
            if event.key == pygame.K_a :
                player1_vitesse = 0
            if event.key == pygame.K_q :
                player1_vitesse = 0

    screen.fill(black)#Background
    
    #Afficher les joueurs :
    Player1.move(player1_vitesse)
    Player2.move(player2_vitesse)
    Player1.afficher(screen)
    Player2.afficher(screen)
    #----#

    if start : 
        #Action de la ball (affichage et bor) =
        if ball.rect.x < 1:
            #ball.velocity[0] = -ball.velocity[0]
            Score_PLayer2 += 1
            start = False
            ball.rect.x = 450
            ball.rect.y = 210
            FPS = 30
        if ball.rect.x > 880 :
            #ball.velocity[0] = -ball.velocity[0]
            Score_Player1 += 1
            start = False
            ball.rect.x = 450
            ball.rect.y = 210
            FPS = 30
        if ball.rect.y < 1 :
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y > 480 :
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.x <= Player1.player_rect.topright[0] and ball.rect.x >= Player1.player_rect.topleft[0] :
            #print('Dans l axe x du pallet 1')
            if ball.rect.y >=  Player1.player_rect.topright[1] and ball.rect.y <= Player1.player_rect.bottomright[1] :
                #print('touche')
                ball.rebond_pallet()
                tour += 1
        if ball.rect.x+20 <= Player2.player_rect.topright[0] and ball.rect.x+20 >= Player2.player_rect.topleft[0] :
            #print('Dans l axe x du pallet 2')
            if ball.rect.y >=  Player2.player_rect.topleft[1] and ball.rect.y <= Player2.player_rect.bottomleft[1] :
                #print('touche')
                ball.rebond_pallet()
                tour += 1
        ball.move(ball.velocity)
        ball.afficher(screen)
        #----#
    else :
        ball.afficher(screen)
        myfont = pygame.font.SysFont("Arial", 14)
        score_display = myfont.render('Press space to start', 1, (255,255,255))
        screen.blit(score_display, (403, 250))
        myfont = pygame.font.SysFont("Impact", 70)
        score_display = myfont.render(str(Score_Player1), 1, (255,255,255))
        screen.blit(score_display, (200, 200))
        myfont = pygame.font.SysFont("Impact", 70)
        score_display = myfont.render(str(Score_PLayer2), 1, (255,255,255))
        screen.blit(score_display, (700, 200))


    #fixer le nombre de fps
    clock.tick(FPS)

    pygame.display.flip()#Actualise
pygame.quit()
quit()