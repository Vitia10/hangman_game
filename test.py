from game import Brain as b
from main import text_read
import unittest

class Tests(unittest.TestCase):
    def setUp(self):
        self.brain = b()
    def test_lose(self):
        if self.brain.wrong_count > 6:      
            self.assertEqual('You lost.Try again!','You lost.Try again!')

if __name__ == '__main__':
    unittest.main()

