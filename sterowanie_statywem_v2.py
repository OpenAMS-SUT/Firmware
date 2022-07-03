import RPi.GPIO as gpio
from time import sleep
import pygame
gpio.setmode(gpio.BCM)
pygame.init()
window=pygame.display.set_mode((250,250))
steppin = 18#29
dirpin = 5#22
steppin2 = 17
dirpin2=27
gpio.setup(dirpin,gpio.OUT)#dir
gpio.setup(steppin,gpio.OUT)#step 25
gpio.output(dirpin,gpio.LOW)
gpio.output(steppin,gpio.LOW)
gpio.setup(dirpin2,gpio.OUT)
gpio.setup(steppin2,gpio.OUT)
gpio.output(dirpin2,gpio.LOW)
gpio.output(steppin2,gpio.LOW)
PR=gpio.HIGH #obrót w prawo
LW =gpio.LOW #obrót w lewo
delay = .002
krok = 0
counter = 0
counter2=0
suma_krokow =0 
suma_krokow2 =0 

def obrot_przeciwny(x):
    wartosc_obrotu = 3094*x
    for krok in range (0,wartosc_obrotu): 
        gpio.output(steppin,gpio.HIGH)
        sleep(delay)
        gpio.output(steppin,gpio.LOW)
        sleep(delay)
        gpio.output(dirpin,LW)

def obrot(x):
    wartosc_obrotu = 3094*x
    for krok in range (0,wartosc_obrotu):
        gpio.output(steppin,gpio.HIGH)
        sleep(delay)
        gpio.output(steppin,gpio.LOW)
        sleep(delay)
        gpio.output(dirpin,PR)
        
def gora(x) :
    wartosc_obrotu =6800*x
    for krok in range(0,wartosc_obrotu):
        gpio.output(steppin2,gpio.HIGH)
        sleep(delay)
        gpio.output(steppin2,gpio.LOW)
        sleep(delay)
        gpio.output(dirpin2,PR)

def dol(x): 
    wartosc_obrotu = 6800*x
    for krok in range(0,wartosc_obrotu):
        gpio.output(steppin2,gpio.HIGH)
        sleep(delay)
        gpio.output(steppin2,gpio.LOW)
        sleep(delay)
        gpio.output(dirpin2,LW)

while True:
    if counter < 6:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    print("klik1")
                    obrot(1)
                    counter += 1
                    suma_krokow = suma_krokow + 3094
                    print(counter)
                    print(suma_krokow)

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_2:
                    print("klik2")
                    obrot_przeciwny(1)
                    counter -= 1
                    suma_krokow = suma_krokow - 3094
                    print(counter)
                    print(suma_krokow) 
    if counter2 >0:
        print("maksymalny wychyl w gore wcisnij s")
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_s:
                    print("klik S")
                    dol(2)
                    suma_krokow2 =0
                    counter2 = 0
                    
    if counter2<0:
        print("maksymalny wychyl w dol wcisnij w")
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    print("klik W")
                    gora(1)
                    suma_krokow2=0
                    counter2 = 0
                    
    if counter2==0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    print("klik W")
                    gora(2)
                    suma_krokow2 = suma_krokow2 + 13600
                    counter2 = 2
                if event.key==pygame.K_s:
                    print("klik S")
                    dol(1)
                    suma_krokow2=suma_krokow2-6800
                    counter2 = -1

    if counter ==6:
        print("Wyzeruj pozycję")
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_3:
                    print("klik3")
                    obrot_przeciwny(counter)
                    counter = 0
                    suma_krokow =0
                    print(counter)
                    print(suma_krokow)

 

            