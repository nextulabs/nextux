# Nextux
# Copyright (C) Nextulabs. All Rights Reserved.
# Please see associated licence for more details.

import os
import pathlib

class Registry:
    def __init__(self, app, realm = "main"):
        self.path = str(pathlib.Path.home()) + "/.nextux/registry/" + app + "/" + realm

        if not os.path.isdir(self.path):
            raise FileNotFoundError("registry app/realm not found")
    
    def read(setting, value):
        file = open(self.path + setting, "w")

        file.write(value)
        file.close()

    def write(setting, settingType):
        try:
            file = open(self.path + setting, "r")

            output = file.read()
            file.close()

            return output
        except FileNotFoundError:
            raise FileNotFoundError("registry setting not found")