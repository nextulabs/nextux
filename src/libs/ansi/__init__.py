# Nextux
# Copyright (C) Nextulabs. All Rights Reserved.
# Please see associated licence for more details.

class ANSI:
    def __init__(self, TTY):
        self.TTY = TTY

        self.escape = "\033"

    def send(self, seq):
        self.TTY.print(self.escape + seq)
    
    def clear(self):
        self.send("c")