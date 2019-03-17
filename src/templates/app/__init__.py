# Nextux
# Copyright (C) Nextulabs. All Rights Reserved.
# Please see associated licence for more details.

APP_DEAD = 0
APP_ALIVE = 1
APP_DORMANT = 2

class Template_App:
    def __init__(self, pid):
        self._state = 1
        self._pid = pid

        self._events_init()
    
    def _events_init(self):
        pass