import time

class Chrono:

    '''Chronograph class.'''

    def __init__(self, autostart=True):
        '''Initialize counter to zero; if autostart, start counting.'''
        self.count = 0
        if autostart:
            self.last = time.perf_counter()
        else:
            self.last = None

    def get(self):
        '''Get elapsed time in seconds since start or last reset; 
        return 0 if not started.'''
        current = time.perf_counter()
        if self.last != None:
            self.count += current - self.last
            self.last = current
        return self.count

    def reset(self, autostop=False):
        '''Reset counter to zero; if not autostop, keep counting.'''
        self.count = 0
        if autostop:
            self.last = None
        elif self.last != None:
            self.last = time.perf_counter()

    def resume(self):
        '''Resume counting; does nothing if not already counting.'''
        if self.last == None:
            self.last = time.perf_counter()
        return self

    def pause(self):
        '''Stop counting; does nothing if already paused.'''
        if self.last != None:
            self.count += time.perf_counter() - self.last
            self.last = None