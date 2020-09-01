from unittest import TestCase
from mijn_simpel.cli import main

class TestConsole(TestCase):
    def test_basic(self):
        main()

if __name__ == '__main__':
    unittest.main()
