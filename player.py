from time import sleep
from machine import UART

class Player:
    
    sleep_time = 0.5
    
    
    def __init__(self):
        
        self.uart = UART(0, baudrate=115200)
        self.uart.init(115200, bits=8, parity=None, stop=1)
        
        self.run_command("AT+VOL=30")
        self.run_command("AT+PLAYMODE=3")
        

    def run_command(self, command):
        self.uart.write(command + "\r\n")
        print(command)
        sleep(self.sleep_time)
        while self.uart.any() == 0:
            sleep(self.sleep_time)
        read = self.uart.readline()
        sleep(self.sleep_time)
        response = read.decode('utf16')
        print(response)
        return response


    def play_file(self, path):
        
        print("Play file: " + path)
        self.run_command("AT+PLAYFILE=" + path)
        
        play_time = self.run_command("AT+QUERY=4")
        #try:
        #    print("Wait for: " + play_time)
        #    sleep(int(play_time))
        #except:
        #    print("Incorrect play time")
