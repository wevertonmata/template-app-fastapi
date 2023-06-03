"""Relative Path & Basic Test"""

try:
    import sys, os

    absolute_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, absolute_path + '/../')
except:
    raise


import unittest


class BasicTest(unittest.TestCase):
    """Basic Test"""
    pass

    @staticmethod
    def main():
        """Unit Test"""
        unittest.main()
