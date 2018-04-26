# playSounds.py

import pygame
'''
def play_for(sample_wave, ms):
    """Play the given NumPy array, as a sound, for ms milliseconds."""
    sound = pygame.sndarray.make_sound(sample_wave)
    sound.play(-1)
    pygame.time.delay(ms)
    sound.stop()

import numpy
import scipy.signal

sample_rate = 44100

def sine_wave(hz, peak, n_samples=sample_rate):
    """Compute N samples of a sine wave with given frequency and peak amplitude.
       Defaults to one second.
    """
    length = sample_rate / float(hz)
    omega = numpy.pi * 2 / length
    xvalues = numpy.arange(int(length)) * omega
    onecycle = peak * numpy.sin(xvalues)
    return numpy.resize(onecycle, (n_samples,)).astype(numpy.int16)

def square_wave(hz, peak, duty_cycle=.5, n_samples=sample_rate):
    """Compute N samples of a sine wave with given frequency and peak amplitude.
       Defaults to one second.
    """
    t = numpy.linspace(0, 1, 500 * 440/hz, endpoint=False)
    wave = scipy.signal.square(2 * numpy.pi * 5 * t, duty=duty_cycle)
    wave = numpy.resize(wave, (n_samples,))
    return (peak / 2 * wave.astype(numpy.int16))



# Play A-440 for 1 second as a square wave:
#play_for(square_wave(440, 4096), 1000)
'''
from time import sleep
from sys import exit
import serial


pygame.init()
pygame.mixer.init(44000, -16, 1, 1024) 
#Cargo los sonidos
sound = [None]*7
sound[0] = pygame.mixer.Sound("./sounds/piano/39191__jobro__piano-ff-044.wav")
sound[1] = pygame.mixer.Sound("./sounds/piano/39193__jobro__piano-ff-045.wav") 
sound[2] = pygame.mixer.Sound("./sounds/piano/39194__jobro__piano-ff-046.wav") 
sound[3] = pygame.mixer.Sound("./sounds/piano/39195__jobro__piano-ff-047.wav") 
sound[4] = pygame.mixer.Sound("./sounds/piano/39196__jobro__piano-ff-048.wav") 
sound[5] = pygame.mixer.Sound("./sounds/piano/39197__jobro__piano-ff-049.wav") 
sound[6] = pygame.mixer.Sound("./sounds/piano/39198__jobro__piano-ff-050.wav")  
#sound[7] = pygame.mixer.Sound("./sounds/piano/39199__jobro__piano-ff-051.wav") 
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
serialFromArduino = serial.Serial("/dev/serial/by-id/usb-Arduino__www.arduino.cc__Arduino_Uno_64935343633351B0D0E1-if00",115200)
serialFromArduino.flush()
arduinoString = serialFromArduino.readline().decode('utf-8') 
sleep(1)

while (len(arduinoString) != 9):
    try:
        arduinoString = serialFromArduino.readline().decode('utf-8') 
        break
    except:
        break

while True:
    try:
        arduinoString = serialFromArduino.readline().decode('utf-8')  #demora mucho
        #arduinoString = serialFromArduino.readline()
        print(arduinoString)
        print(arduinoString[len(arduinoString)-3])
        print(len(arduinoString))
        if(len(arduinoString)==9):
            for x in range(0,7):
                nota[x] = int(arduinoString[x])
                print(str(nota[x]) + '\n')
                if(nota[x]==0):
                    print(x)
                    canal[x].play(sound[x])
                    # Play A (440Hz) for 1 second as a sine wave:
                    #play_for(sine_wave(440, 4096), 1000)
                    
            '''
            if (nota[0] == 0):
                print("sape")
                canal[0].play(sound[0]) 
                    

            if (nota[1] == 0):
                canal[1].play(sound[1]) 
            '''
            

        

    except KeyboardInterrupt: 
        exit()