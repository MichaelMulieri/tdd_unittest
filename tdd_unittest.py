import unittest

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

def isOdd(n):
    if n % 3 == 0:
        return True
    else:
        return False

class IsEvenTests(unittest.TestCase):

    def testTwo(self):
        self.assertEqual(isEven(2), True)

    def testThree(self):
        self.assertEqual(isEven(3), False)

    def testFour(self):
        self.assertEqual(isEven(4), True)

    def testFive(self):
        self.assertEqual(isEven(5), False)

    def setUp(self):
        print("running setUp")

    def tearDown(self):
        print("running tearDown tasks")

class IsOddTests(unittest.TestCase):

    def testThree(self):
        self.assertEqual(isOdd(3), True)

    def testFour(self):
        self.assertEqual(isOdd(4), False)

if __name__ == "__main__":
    unittest.main()

    
