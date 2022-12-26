from time import sleep
from machine import UART, Pin

from player import Player


print("Starting...\n")


player = Player()

button1 = Pin(15, Pin.IN)
button2 = Pin(14, Pin.IN)
button3 = Pin(13, Pin.IN)
button4 = Pin(12, Pin.IN)
button5 = Pin(11, Pin.IN)
button6 = Pin(10, Pin.IN)

while True:
    print()
    print("Button 1: " + str(button1.value()))
    print("Button 2: " + str(button2.value()))
    print("Button 3: " + str(button3.value()))
    print("Button 4: " + str(button4.value()))
    print("Button 5: " + str(button5.value()))
    print("Button 6: " + str(button6.value()))


    print()

    if button1.value():
        player.play_file("/00/001.mp3")
        
    elif button2.value():
        player.play_file("/00/002.mp3")
    
    elif button3.value():
        player.play_file("/00/003.mp3")
        
    elif button4.value():
        player.play_file("/00/004.mp3")
    
    elif button5.value():
        player.play_file("/00/005.mp3")
        
    elif button6.value():
        player.play_file("/00/006.mp3")
        
    sleep(0.5)
