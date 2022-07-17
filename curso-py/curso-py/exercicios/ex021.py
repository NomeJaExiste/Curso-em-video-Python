import pygame
from pygame import mixer, event
mixer.init()
pygame.init()
mixer.music.load(r'C:\Users\isaqu\OneDrive\Área de Trabalho\programação\curso-py\exercicios\ex021.mp3')
mixer.music.play()
event.wait()