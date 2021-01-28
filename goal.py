import os, time
from gpiozero import LED
from signal import pause

led = LED(17)

def activate_experience():
    led.on()
    play_horn()
    led.off()
    

def play_horn():
    #os.system('sudo ./autopair') # Ensure our speaker is still paired with out rpi
    #time.sleep(1)
    os.system('cvlc static/media/Carolina_Hurricanes.mp3 vlc://quit')