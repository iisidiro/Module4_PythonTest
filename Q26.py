import unittest

def name(name):
    return name

class myTest(unittest.TestCase):

    def test(self):

        self.assertEqual(name("MIGUEL"),"MIGUEL")

if __name__ == '__main__':

    unittest.main()