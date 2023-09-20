import pygame
from random import randint
from math import sqrt, pow
from pygame import mixer

# Iniciando pygame/ Initializing pygame
pygame.init()

# Configuração de tela / Sreen config
screen = pygame.display.set_mode((1024,768))

# Background
background =  pygame.image.load("backgroundPOTG.png")

# Background music
mixer.music.load("MCR - WTTBP_midi.wav")
mixer.music.play(-1)

# Titulo e ícone / Title and icon
pygame.display.set_caption("Protector of the Galaxy")
icon = pygame.image.load('iconPOTG.ico')
pygame.display.set_icon(icon)

explosion_ico = pygame.image.load("explosionICO.ico")
explosion_ico_x = 0
explosion_ico_y = 0

# Jogador / Player
player_img = pygame.image.load("playerPOTG.ico")
player_x = 480
player_y = 690
player_x_change = 0

# Monstros / Mobs

mob1_img = []
mob1_x = []
mob1_y = []
mob1_x_change = []
mob1_y_change = []
num_of_mob1 = 2

for i in range(num_of_mob1): 
    mob1_img.append(pygame.image.load("alien1.ico"))
    mob1_x.append(randint(0, 960))
    mob1_y.append(0)
    mob1_x_change.append(2)
    mob1_y_change.append(0.05)


mob2_img = []
mob2_x = []
mob2_y = []
mob2_x_change = []
mob2_y_change = []
num_of_mob2 = 2

for i in range(num_of_mob2): 
    mob2_img.append(pygame.image.load("alien2.ico"))
    mob2_x.append(randint(0, 960))
    mob2_y.append(0)
    mob2_x_change.append(2)
    mob2_y_change.append(0.05)    

mob3_img = []
mob3_x = []
mob3_y = []
mob3_x_change = []
mob3_y_change = []
num_of_mob3 = 2

for i in range(num_of_mob3): 
    mob3_img.append(pygame.image.load("alien3.ico"))
    mob3_x.append(randint(0, 960))
    mob3_y.append(0)
    mob3_x_change.append(2)
    mob3_y_change.append(0.05)


boss_img = pygame.image.load("polvoREI.png")
boss_x = randint(0, 896)
boss_y = 0
boss_x_change = 2
boss_y_change = 0.05

boss_life = 3
font = pygame.font.Font('freesansbold.ttf', 32)

boss_life_x = 800
boss_life_y = 10

# Projéteis / Bullets // ready(cant see on the screen) fire(on the move)

bullet_img = pygame.image.load("projetilPOTG.ico")
bullet_x = 0
bullet_y = 700
bullet_x_change = 0
bullet_y_change = 15
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

text_x = 10
text_y = 10

over_font = pygame.font.Font("freesansbold.ttf", 64)

congratulations_font = pygame.font.Font("freesansbold.ttf", 64)

    
def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (400, 340))

def zerou_o_jogo_text():
    congratulations_text = font.render("CONGRATULATIONS", True, (255, 255, 255))
    screen.blit(congratulations_text, (350, 340))

def show_boss_life(x,y):
    score = font.render("Boss life: " + str(boss_life), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(player_img, (x, y))

def mob1(x, y, i):
    screen.blit(mob1_img[i], (x, y))

def mob2(x, y, i):
    screen.blit(mob2_img[i], (x, y))   

def mob3(x, y, i):
    screen.blit(mob3_img[i], (x, y))

def boss(x, y):
    screen.blit(boss_img, (x, y))

def explosion_contact(x, y):
    screen.blit(explosion_ico, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 13))

def is_collision_mob1(mob1_x, mob1_y, bullet_x, bullet_y):
    distance = sqrt((pow(mob1_x - bullet_x, 2)) + (pow(mob1_y - bullet_y, 2)))
    if distance < 27:
        return True
    else: 
        return False

def is_collision_mob2(mob2_x, mob2_y, bullet_x, bullet_y):
    distance = sqrt((pow(mob2_x - bullet_x, 2)) + (pow(mob2_y - bullet_y, 2)))
    if distance < 27:
        return True
    else: 
        return False
    
def is_collision_mob3(mob3_x, mob3_y, bullet_x, bullet_y):
    distance = sqrt((pow(mob3_x - bullet_x, 2)) + (pow(mob3_y - bullet_y, 2)))
    if distance < 27:
        return True
    else: 
        return False

def is_collision_boss(boss_x, boss_y, bullet_x, bullet_y):
    distance = sqrt((pow(boss_x - bullet_x, 2)) + (pow(boss_y - bullet_y, 2)))
    if distance < 75:
        return True
    else: 
        return False


# Game loop
game = True
boss_state = False
running = True
while running:

    # RGB -  red  green  blue
    screen.fill((0, 0, 0))
    # Backgroung image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -8
            if event.key == pygame.K_RIGHT:
                player_x_change = 8
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0   

    # player bounderies
    player_x += player_x_change
    if player_x  <= 0:
        player_x = 0
    elif player_x >= 960:
        player_x = 960

    # count é o contador de ticks do jogo, 4800 ticks equivale a aproximadamente 60s. A cada min a velocidade do mob no eixo y aumenta
    count = 0

    if score_value >= 50 :
        boss_state = True


    collision_sound = mixer.Sound("explosion.wav")

    for i in range(num_of_mob1):

        if mob1_y[i] > 660:
            if boss_state == True:
                boss_y = -2000000
            for j in range(num_of_mob1):
                mob1_y[j] = -2000000
            for j in range(num_of_mob2):
                mob2_y[j] = -2000000
            for j in range(num_of_mob3):
                mob3_y[j] = -2000000
            game = False
            break
            

        mob1_x[i] += mob1_x_change[i]
        mob1_y[i] += mob1_y_change[i]
        if mob1_x[i] <= 0:
            mob1_x_change[i] = 2
        elif mob1_x[i] >= 960:
            mob1_x_change[i] = -2
        if count % 4800 == 0:
            mob1_y_change[i] += 0.0002
        
        collision_mob1 = is_collision_mob1(mob1_x[i], mob1_y[i], bullet_x, bullet_y)
        if collision_mob1:
            explosion_contact(mob1_x[i], mob1_y[i])
            collision_sound.play()
            bullet_y = 704
            bullet_state = "ready"
            score_value += 1
            explosion_contact(mob2_x[i], mob2_y[i])
            mob1_x[i] = randint(0, 960)
            mob1_y[i] = 0

        mob1(mob1_x[i], mob1_y[i], i)

    for i in range(num_of_mob2):

        if mob2_y[i] > 660:
            if boss_state == True:
                boss_y = -2000000
            for j in range(num_of_mob1):
                mob1_y[j] = -2000000
            for j in range(num_of_mob2):
                mob2_y[j] = -2000000
            for j in range(num_of_mob3):
                mob3_y[j] = -2000000
            game = False
            break
            

        mob2_x[i] += mob2_x_change[i]
        mob2_y[i] += mob2_y_change[i]
        if mob2_x[i] <= 0:
            mob2_x_change[i] = 2
        elif mob2_x[i] >= 960:
            mob2_x_change[i] = -2
        if count % 4800 == 0:
            mob2_y_change[i] += 0.0002

        collision_mob2 = is_collision_mob2(mob2_x[i], mob2_y[i], bullet_x, bullet_y)
        if collision_mob2:
            explosion_contact(mob2_x[i], mob2_y[i])
            collision_sound.play()
            bullet_y = 704
            bullet_state = "ready"
            score_value += 1
            explosion_contact(mob2_x[i], mob2_y[i])
            mob2_x[i] = randint(0, 960)
            mob2_y[i] = 0


        mob2(mob2_x[i], mob2_y[i], i)
    
    for i in range(num_of_mob3):

        if mob3_y[i] > 660:
            if boss_state == True:
                boss_y = -2000000
            for j in range(num_of_mob1):
                mob1_y[j] = -2000000
            for j in range(num_of_mob2):
                mob2_y[j] = -2000000
            for j in range(num_of_mob2):
                mob3_y[j] = -2000000            
            game = False
            break

        mob3_x[i] += mob3_x_change[i]
        mob3_y[i] += mob3_y_change[i]
        if mob3_x[i] <= 0:
            mob3_x_change[i] = 2
        elif mob3_x[i] >= 960:
            mob3_x_change[i] = -2
        if count % 4800 == 0:
            mob3_y_change[i] += 0.0002

        mob3(mob3_x[i], mob3_y[i], i)

        collision_mob3 = is_collision_mob3(mob3_x[i], mob3_y[i], bullet_x, bullet_y)
        if collision_mob3:
            explosion_contact(mob2_x[i], mob2_y[i])
            collision_sound.play()
            bullet_y = 704
            bullet_state = "ready"
            score_value += 1
            explosion_contact(mob2_x[i], mob2_y[i])
            mob3_x[i] = randint(0, 960)
            mob3_y[i] = 0

    count += 1
    
    #bullet movement
    if bullet_y <= 0:
        bullet_y = 704
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    if boss_state == True:
        show_boss_life(boss_life_x, boss_life_y)

        if boss_y > 660:
            boss_y = -2000000
            for j in range(num_of_mob1):
                mob1_y[j] = -2000000
            for j in range(num_of_mob2):
                mob2_y[j] = -2000000
            for j in range(num_of_mob3): 
                mob3_y[j] = -2000000
            game = False
            break
            

        boss_x += boss_x_change
        boss_y += boss_y_change
        if boss_x <= 0:
            boss_x_change = 2
        elif boss_x >= 896:
            boss_x_change = -2
        if boss_y >= 550:
            boss_y = randint(0, 250)
        if count % 4800 == 0:
            boss_y_change += 0.0001

        collision_boss = is_collision_boss(boss_x, boss_y, bullet_x, bullet_y)
        if collision_boss:
            explosion_contact(mob2_x[i], mob2_y[i])
            collision_sound.play()
            bullet_y = 704
            bullet_state = "ready"
            boss_life -= 1
            explosion_contact(mob2_x[i], mob2_y[i])
        if boss_life == 0:
            boss_y = -2000000
            for j in range(num_of_mob1):
                mob1_y[j] = -2000000
            for j in range(num_of_mob2):
                mob2_y[j] = -2000000
            for j in range(num_of_mob3): 
                mob3_y[j] = -2000000
            game = False

        boss(boss_x, boss_y)
    
    if game == False:
        if boss_life == 0:
            zerou_o_jogo_text()
        else:
            game_over_text()
    
    player(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()


