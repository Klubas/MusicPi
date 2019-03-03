#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
from time import sleep

GPIO.setmode(GPIO.BOARD)

class Tone:
    def __init__(self, note, duration=0):
        self.note = note
        self.duration = duration
        self.frequency = note.frequency

class Note:
    def __init__(self, note, frequency, mult=0.2):
        self.note = note
        self.frequency = frequency * mult
    
    def H(self):
        if len(self.note) == 1:        
            self.note = self.note + 'H'
        elif len(self.note) == 2:
            self.note = self.note + 'H'
        self.frequency = (self.frequency * 2) + 1
        return self

    def S(self):
        if len(self.note) == 1:
            self.note = self.note + 'S'
        elif len(self.note == 2):
            self.note = self.note + 'S'
        self.frequency = self.frequency + ((self.frequency * 2) / 32)#??
        return self


class Scale:
    def __init__(self):
        self.notas = {
            'a'  :  440,
            'b'  :  466,
            'c'  :  261, 
            'd'  :  294,
            'e'  :  329,
            'f'  :  349,
            'g'  :  391,
            't'  :    1 #tempo
            #'gS' :  Note('gS', 415),
            #'aS' :  Note('aS', 455),
            #'cH' :  Note('cH', 523),
            #'cSH':  Note('cSH',554),
            #'dH' :  Note('dH', 587),
            #'dSH':  Note('dSH',622),
            #'eH' :  Note('eH', 659),
            #'fH' :  Note('fH', 698),
            #'fSH':  Note('fSH',740),
            #'gH' :  Note('gH', 784),
            #'gSH':  Note('gSH',830),
            #'aH' :  Note('aH', 880)
        }
        
    def calculeNota(self, n):
        base = Note(n[0], self.notas[n[0]])

        if len(n) >= 2:
            if n[1] == 'S':
                base = base.S()
            elif n[1] == 'H':
                base = base.H()
        
        if len(n) >= 3:
            if n[2] == 'S':
                base = base.S()
            if n[2] == 'H':
                base = base.H()

        print(base.note + ' ' + str(base.frequency))
        return base

    def note(self, n):
        return self.calculeNota(n)

class Buzzer:
    def __init__(self, pin, dutyCycle=15, interval=20):
        self.pin=pin
        self.dutyCycle=dutyCycle
        self.interval=interval
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        self.p = GPIO.PWM(self.pin, 1)

    def beep(self, tone):
        self.p.stop()
        self.p = GPIO.PWM(self.pin, tone.frequency)
        self.p.start(0)
        self.p.ChangeDutyCycle(self.dutyCycle)
        self.wait(tone.duration)
        self.p.ChangeDutyCycle(0)
        self.p.stop()
        self.wait(self.interval)

    def start_beep(self, tone):
        self.p.stop()
        self.p = GPIO.PWM(self.pin, tone.frequency)
        self.p.start(0)
        self.p.ChangeDutyCycle(self.dutyCycle)

    def stop_beep(self):
        #self.p = GPIO.PWM(self.pin, tone.frequency)
        self.p.ChangeDutyCycle(0)
        self.p.stop()

    def wait(self, time):
        sleep(time * 0.001)

class Play:
    def __init__(self):
        self.s = Scale()
        self.b = Buzzer(12)

    def play_note(self, note):
        note = self.s.note(note)
        #self.b.beep(Tone(note))
        self.b.start_beep(Tone(note))
    
    def stop_note(self):
        self.b.stop_beep()

    def read_and_play(self, partitura):
        for i in partitura:
            #partitura = [['a', 261].['b', 294],['gH', 192] ... [...]]
            note = self.s.note(i[0])
            duration = i[1]
            if note == 'time':
                self.b.wait(duration)
            else:
                self.b.beep(Tone(note, duration))
                sleep(0.01)

