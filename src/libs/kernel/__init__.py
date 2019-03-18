# Nextux
# Copyright (C) Nextulabs. All Rights Reserved.
# Please see associated licence for more details.

import libs.tty
import libs.ansi
import libs.procman
import apps.init

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
        self.TTY.println("")
        
        self.ProcessManager = libs.procman.ProcessManager()

        self.ProcessManager.new(apps.init.Init)