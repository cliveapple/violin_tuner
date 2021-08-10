"""made by clive hunt 10/08/21"""
import numpy as np
from math import pi
import time
import soundfile as sf
import sounddevice as sd
from scipy.io.wavfile import write
from tkinter import *
#set the notes out by freq
G=196
A=440
D=293
E=695

sps = 44100#sound per second
duration = 5000
atten = 3.0#volume

window = Tk()
window = Canvas(window,width=500,height=700)
window.pack()
image=PhotoImage(file="C:\\Users\\d\\PycharmProjects\\soundtuner\\venv\\image\\violin.png")
#window.create_image(0,0, anchor = NW, image = image)
image1 =PhotoImage(file="C:\\Users\\d\\PycharmProjects\\soundtuner\\venv\\image\\Gnoteviolin.png")
#window.create_image(0,0, anchor = NW, image = image1)
image2 =PhotoImage(file="C:\\Users\\d\\PycharmProjects\\soundtuner\\venv\\image\\Dnoteviolin.png")
#window.create_image(0,0, anchor = NW, image = image2)
image3 = PhotoImage(file=("C:\\Users\\d\\PycharmProjects\\soundtuner\\venv\\image\\Anoteviolin.png"))
#window.create_image(0,0,anchor=NW, image=image3)
image4 = PhotoImage(file=("C:\\Users\\d\\PycharmProjects\\soundtuner\\venv\\image\\Enoteviolin.png"))
#window.create_image(0,0,anchor=NW, image=image4)



x = input("enter a note: \n")
x = x.upper()#coverts user input to be upper case
print(x)

def note_G():
    sample = np.arange(duration * G)
    waveform = np.sin(2 * np.pi * sample * G / sps)
    wave_quiet = waveform * atten
    sd.play(waveform, sps)
    time.sleep(3)
    sd.stop()
def note_A():
    sample = np.arange(duration * A)
    waveform = np.sin(2 * np.pi * sample * A / sps)
    wave_quiet = waveform * atten
    sd.play(waveform, sps)
    time.sleep(3)
    sd.stop()
def note_D():
    sample = np.arange(duration * D)
    waveform = np.sin(2 * np.pi * sample * D / sps)
    wave_quiet = waveform * atten
    sd.play(waveform, sps)
    time.sleep(3)
    sd.stop()
def note_E():
    sample = np.arange(duration * E)
    waveform = np.sin(2 * np.pi * sample * E / sps)
    wave_quiet = waveform * atten
    sd.play(waveform, sps)
    time.sleep(3)
    sd.stop()



if __name__ == '__main__':
    if x == 'G':
        note_G()
        window.create_image(0,0,anchor =NW,image=image1)#loads the image
    if x == 'D':
        note_D()
        window.create_image(0, 0, anchor=NW, image=image2)
    if x == 'A':
        note_A()
        window.create_image(0, 0, anchor=NW, image=image3)

    if x == 'E':
        note_E()
        window.create_image(0, 0, anchor=NW, image=image4)

    window.wait_window()
