#!/usr/bin/python
import sys
import pygame as pg
import RPi.GPIO as GPIO

from MusicalScale import Play 

pg.init()
BLACK = (0,0,0)
WIDTH = 600
HEIGHT = 480
windowSurface = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)
windowSurface.fill(BLACK)

try:
    p = Play()

    if sys.argv[1] == "-t" and sys.argv[2] == "kbd":
        while True:
            pressed = pg.key.get_pressed()
            modif = ''

            if pressed[pg.K_a]:
                modif = 'S'

            if pressed[pg.K_s]:
                modif = modif + 'H'

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_z:
                        p.play_note('a' + modif)  
                    if event.key == pg.K_x:
                        p.play_note('b' + modif)
                    if event.key == pg.K_c:
                        p.play_note('c' + modif)
                    if event.key == pg.K_v:
                        p.play_note('d' + modif)
                    if event.key == pg.K_b:
                        p.play_note('e' + modif)
                    if event.key == pg.K_n:
                        p.play_note('f' + modif)
                    if event.key == pg.K_m:
                        p.play_note('g' + modif)

                if event.type == pg.KEYUP:
                #if event.key == pg.K_a: #nao precisa ter um para cada tecla, considerando que o buzzer s toca um som por vez
                    p.stop_note()

                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
    else:
        while(True):
            p.read_and_play([
                ['a',  500], 
                ['a',  500], 
                ['a',  500], 
                ['f',  350],
                ['cH', 150],
                ['a',  500],
                ['f',  350],
                ['cH', 150],
                ['a',  650],
                ['t',  150],
                ['eH', 500],
                ['eH', 500],
                ['eH', 500],
                ['fH', 350],
                ['cH', 150],
                ['gS', 500],
                ['f',  350],
                ['cH', 150],
                ['a',  650],
                ['t',  150],
                ['aH', 500],
                ['a',  300],
                ['a',  150],
                ['aH', 400],
                ['gSH',200],
                ['gH', 200],
                ['fSH',125],
                ['fH', 125],
                ['fSH',250],
                ['t',  250],
                ['aS', 250],
                ['dSH',400],
                ['dH', 200],
                ['cSH',200],
                ['cH', 125],
                ['b',  125],
                ['cH', 250],
                ['t',  250],
                ['f',  250],
                ['gS', 500],
                ['f',  375],
                ['cH', 125],
                ['a',  500],
                ['f',  375],
                ['cH', 125],
                ['a',  650],
                ['t',  1000]    
        ])
except KeyboardInterrupt:
    print("End")
except Exception as e:
    print(e)
finally:
    GPIO.cleanup()

