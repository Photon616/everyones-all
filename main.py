import random
import time
import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Assets/Audios/glitchrun.wav")
pygame.mixer.music.set_volume(0.9)

screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("test")

clock = pygame.time.Clock()

# image load
checkerboard_img = pygame.image.load("Assets/Textures/uvChecker1k.png")
checkerboard_img = pygame.transform.scale(checkerboard_img, (1024, 1024))

# audio load
death_sound = pygame.mixer.Sound('Assets/Audios/death_glitch.wav')
death_sound.set_volume(0.6)

# variables


# classes

# functions

def start_screen():


    running = True
    keys = pygame.key.get_pressed()

    while running:
        # initiallize the screen
        screen.fill((0, 0, 0))
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()

    # to be finished

def gameOverScreen():


    while running:
        # initiallize the screen
        screen.fill((0, 0, 0))
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()
    
    # pygame.time.wait(1000)

def in_game():
    

    running = True
    while running:
        # initiallize the screen
        screen.fill((0, 0, 0))
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # update sprites' position and the screen itself
        pygame.display.update()

    pygame.quit()
    return

def main():
    state = "start"
    while True:
        if state == "start":
            state = start_screen()
        elif state == "game":
            state = in_game()
        elif state == "gameover":
            state = gameOverScreen()
        else:
            break

    pygame.quit()
    return

# 음악 재생 (이미 mixer.init()이 한 번 되어 있다고 가정)
pygame.mixer.music.set_volume(0.9)
pygame.mixer.music.load("Assets/Audios/glitchrun.wav")
pygame.mixer.music.play(-1)  # 반복 재생

#initial start
main()
