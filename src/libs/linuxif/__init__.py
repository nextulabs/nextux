# Nextux
# Copyright (C) Nextulabs. All Rights Reserved.
# Please see associated licence for more details.

import subprocess
import select

def NULL():
    pass

class LinuxInterface_Command:
    def __init__(self, command):
        self.command = command

        self.stdout = ""
        self.stderr = ""
        self.finished = False

        self.Subprocess = subprocess.Popen(self.command, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    
    def __del__(self):
        self.Subprocess.kill()
    
    def poll(self):
        if not self.finished:
            broken = False

            while self.Subprocess.stdout in select.select([self.Subprocess.stdout], [], [], 0)[0]:
                line = self.Subprocess.stdout.readline()

                if line and line != b"":
                    self.stdout += line.decode("utf-8").replace("\n", "\r\n")
                else:
                    broken = True
                    break
            
            if broken:
                self.finished = True
                
                return False
            else:
                broken = False

                while self.Subprocess.stderr in select.select([self.Subprocess.stderr], [], [], 0)[0]:
                    line = self.Subprocess.stderr.readline()

                    if line and line != b"":
                        self.stdout += line.decode("utf-8").replace("\n", "\r\n")
                    else:
                        broken = True
                        break
                
                if broken:
                    self.finished = True
                    
                    return False
                else:
                    return True
        else:
            return False
    
    def writestdin(self, text):
        if not self.finished:
            try:
                self.Subprocess.stdin.write(text.encode())
                self.Subprocess.stdin.flush()

                return True
            except BrokenPipeError:
                return False
        else:
            return False
    
    def readstdout(self):
        stdout = self.stdout
        self.stdout = ""

        return stdout
    
    def readstderr(self):
        stderr = self.stderr
        self.stderr = ""

        return stderr