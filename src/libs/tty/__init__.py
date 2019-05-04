# Nextux
# Copyright (C) Nextulabs. All Rights Reserved.
# Please see associated licence for more details.

import serial
import os
import libs.ansi

class TTY:
    def __init__(self, console = "tty"):
        self.console = "/dev/" + console
        
        self.Serial = serial.Serial()
        self.Serial.port = self.console
        self.Serial.open()
        self.Serial.flushInput()
        self.Serial.flushOutput()

        self.ANSI = libs.ansi.ANSI(self)
    
    def __del__(self):
        self.Serial.close()
    
    def print(self, text):
        self.Serial.write(text.encode())

    def println(self, text):
        self.print(text + "\r\n")
    
    def read(self, count = 1):
        return self.Serial.read(count).decode("utf-8")
    
    def readln(self, show = True):
        text = ""
        char = ""

        scrlenc, scrlenr = os.get_terminal_size(0)

        while char != "\r":
            if len(text) > 0: self.ANSI.send("[" + str(min(len(text), scrlenc - 2)) + "C")

            char = self.read()

            if len(text) > 0: self.ANSI.send("[" + str(min(len(text), scrlenc - 2)) + "D")

            if ord(char) == 127:
                if len(text) > 0:
                    text = text[:-1]
            else:
                text += char

            self.print((text + " ")[-(scrlenc - 1):])
            self.ANSI.send("[" + str(min(len(text) + 1, scrlenc - 1)) + "D")

        self.println("")

        return text