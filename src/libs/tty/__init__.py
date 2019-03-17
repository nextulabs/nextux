# Nextux
# Copyright (C) Nextulabs. All Rights Reserved.
# Please see associated licence for more details.

import serial

class TTY:
    def __init__(self, console = "tty"):
        self.console = "/dev/" + console
        
        self.Serial = serial.Serial()
        self.Serial.port = self.console
        self.Serial.open()
        self.Serial.flushInput()
        self.Serial.flushOutput()
    
    def __del__(self):
        self.Serial.close()
    
    def print(self, text):
        self.Serial.write(text.encode())

    def println(self, text):
        self.print(text + "\r\n")