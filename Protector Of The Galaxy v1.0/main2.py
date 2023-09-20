import pygame

# Iniciando pygame/ Initializing pygame
pygame.init()

# Configuração de tela / Sreen config
screen = pygame.display.set_mode((800,600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# checkpoint