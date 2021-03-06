# Nextux
# Copyright (C) Nextulabs. All Rights Reserved.
# Please see associated licence for more details.

import templates.app
import libs.tty

class Init(templates.app.Template_App):
    def _events_init(self, args = []):
        self.TTY = libs.tty.TTY()

        self.TTY.println("Initialised!")
        self.TTY.print("Type something: ")

        self.TTY.println("You said: " + self.TTY.readln())

        import time; time.sleep(1)