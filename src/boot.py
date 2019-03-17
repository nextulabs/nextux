# Nextux
# Copyright (C) Nextulabs. All Rights Reserved.
# Please see associated licence for more details.

try:
    import serial
except ImportError:
    raise ImportError("one or more 3rd-party libraries are not installed and they are needed to boot")

import os

import libs.kernel

try:
    kernel = libs.kernel.Kernel({
        "name": "Nextux",
        "version": "V0.1.0",
        "copyright": "Copyright (C) Nextulabs. All Rights Reserved.",
        "extraInfo": "Please see the associated licence for more details."
    })
    
    os.system("reset")
except KeyboardInterrupt:
    os.system("reset")