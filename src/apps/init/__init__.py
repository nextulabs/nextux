# Nextux
# Copyright (C) Nextulabs. All Rights Reserved.
# Please see associated licence for more details.

import templates.app
import libs.tty

class Init(templates.app.Template_App):
    def _events_init(self):
        self.TTY = libs.tty.TTY()

        self.TTY.println("Initialised!")