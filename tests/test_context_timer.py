
import time
import unittest

import context_timer

class TestContextTimer(unittest.TestCase):

    def test_time(self):
        with context_timer.ContextTimer():
            time.sleep(1)

if __name__ == '__main__':
    unittest.main()