import time

class ContextTimer(object):
    def __enter__(self):
        self.t = time.time()
    def __exit__(self, type, value, traceback):
        print('time elapsed: {:.8f}'.format(time.time() - self.t))