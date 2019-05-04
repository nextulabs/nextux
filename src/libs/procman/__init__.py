# Nextux
# Copyright (C) Nextulabs. All Rights Reserved.
# Please see associated licence for more details.

class ProcessManager:
    def __init__(self):
        self.processes = []

    def new(self, app, args = []):
        newProc = app(len(self.processes), args)
        self.processes.append(newProc)

        return len(self.processes) - 1
    
    def kill(self, pid):
        self.processes[pid]._events_kill()