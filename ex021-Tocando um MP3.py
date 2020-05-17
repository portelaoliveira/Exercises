'''
EXERCÍCIO 021: Tocando um MP3

Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

from pygame import mixer
from time import sleep

mixer.init()
mixer.music.load('ex021.mp3.mp3')
mixer.music.play()
sleep(300)
