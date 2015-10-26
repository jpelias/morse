#! /usr/bin/env python
 
import pygame
import time
import sys

from array import array
from time import sleep

from pygame.mixer import Sound, get_init, pre_init


CODE = {'.-' :'A',     '-...':'B',   '-.-.':'C', 
        '-..':'D',    '.':'E',      '..-.':'F',
        '--.':'G',    '....':'H',   '..':'I',
        '.---':'J',   '-.-':'K',    '.-..':'L',
        '--':'M',     '-.': 'N',     '---': 'O',
        '.--.': 'P',   '--.-': 'Q',   '.-.': 'R',
     	'...': 'S',    '-': 'T',      '..-': 'U',
        '...-': 'V',   '.--': 'W',    '-..-': 'X',
        '-.--': 'Y',   '--..': 'Z',
        
        '-----': '0',  '.----': '1',  '..---': '2',
        '...--': '3',  '....-': '4',  '.....': '5',
        '-....': '6',  '--...': '7',  '---..': '8',
        '----.': '9',  '': " " , '.-.-': ''
        }

# Duracion de un punto
cw = 0.05
 
LEFT = 1
 
running = 1
screen = pygame.display.set_mode((320, 200))

nopulsado = (time.clock())
letra = ""
pulsado = 0


pre_init(22500, -8, 1, 1024)
pygame.init()




class Note(Sound):

    def __init__(self, frequency, volume=.1):
        self.frequency = 2*frequency # Eliminar el 2 si se usa sample rate de 44100
        Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
        for time in xrange(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples

 
 
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
        
    tiempo_nopulsado = (time.clock() - nopulsado)
    
    if tiempo_nopulsado > cw * 5 : 
        
        
        print CODE[letra],letra
        letra = ""
        nopulsado = (time.clock())
        
        
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
        # print "You pressed the left mouse button at (%d, %d)" % event.pos
        pulsado = (time.clock())
        Note(880).play(-1)
        
        
    elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
        pygame.mixer.stop()
        tiempo_pulsado = (time.clock() - pulsado)
        nopulsado = (time.clock())
        
        # print "You released the left mouse button at (%d, %d)" % event.pos
        if  tiempo_pulsado > cw * 2 : 
            letra = letra + "-"
            
            
                        
        if tiempo_pulsado < cw * 2 : 
            letra = letra + "."
            
            
        
        
    screen.fill((0, 0, 0))
    pygame.display.flip()
    
    
