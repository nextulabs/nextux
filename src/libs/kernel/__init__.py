# Nextux Virtual Machine
# Copyright (C) Nextulabs. All Rights Reserved.
# Please see associated licence for more details.

import libs.tty
import libs.ansi

class Kernel:
    def __init__(self, OSInfo):
        self.OSInfo = OSInfo

        self.TTY = libs.tty.TTY()
        self.ANSI = libs.ansi.ANSI(self.TTY)

        self.ANSI.clear()

        self.TTY.println(self.OSInfo["name"] + " [" + self.OSInfo["version"] + "]")
        self.TTY.println(self.OSInfo["copyright"])
        self.TTY.println("")
        self.TTY.println(self.OSInfo["extraInfo"])