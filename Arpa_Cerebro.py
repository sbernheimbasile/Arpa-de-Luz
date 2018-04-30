

import pygame
from time import sleep
from sys import exit
import serial


pygame.init()
pygame.mixer.init(44100, -16, 1, 1024) 

#Cargo los sonidos
sound = [None]*7
sound[0] = pygame.mixer.Sound("./Do.wav")
sound[1] = pygame.mixer.Sound("./Re.wav") 
sound[2] = pygame.mixer.Sound("./Mi.wav") 
sound[3] = pygame.mixer.Sound("./Fa.wav") 
sound[4] = pygame.mixer.Sound("./Sol.wav") 
sound[5] = pygame.mixer.Sound("./La.wav") 
sound[6] = pygame.mixer.Sound("./Si.wav")  


canal = [None]*7
canal[0] = pygame.mixer.Channel(1)
canal[1] = pygame.mixer.Channel(2) 
canal[2] = pygame.mixer.Channel(3) 
canal[3] = pygame.mixer.Channel(4) 
canal[4] = pygame.mixer.Channel(5) 
canal[5] = pygame.mixer.Channel(6)
canal[6] = pygame.mixer.Channel(7)
nota = 10*[None];



print("Sampler Ready.")
'''
serialFromArduino = serial.Serial("/dev/serial/by-id/usb-Arduino__www.arduino.cc__Arduino_Uno_64935343633351B0D0E1-if00",115200)
serialFromArduino.flush()
arduinoString = serialFromArduino.readline().decode('utf-8') 

sleep(1)

#Me salteo la inicializacion de la comunicacion serial.
while (len(arduinoString) != 9):
    try:
        arduinoString = serialFromArduino.readline().decode('utf-8') 
        break
    except:
        break
'''
while True:
        '''
        arduinoString = serialFromArduino.readline().decode('utf-8') 
        print(arduinoString)
        print(arduinoString[len(arduinoString)-3])
        print(len(arduinoString))
        '''            
        string = input("Enter your input: ")                   
        arduinoString = string
        #if(len(arduinoString)==9): #verifico que el mensaje del serial sea el que yo espero.
        if(len(arduinoString)==7):

            for x in range(0,7):
                nota[x] = int(arduinoString[x])
                print(str(nota[x]) + '\n')
                if(nota[x]==0):    #Si se detecta un sensor tapado se reproduce la nota.
                    print(x)
                    if not (canal[x].get_busy()):
                        canal[x].play(sound[x])
                        print("Paso por aca")

                else:
                    if (canal[x].get_busy()):  #Si el sensor no esta tapado pero esta sonando el tono, lo apago haciendole un fadeout para que no se abrupto.
                        canal[x].fadeout(1000)
