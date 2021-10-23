import unittest
from commonss import LinkedList

class TestCorrectness(unittest.TestCase):
    def testLinkedList_1(self):
        l = LinkedList()
        l.push1("a")
        l.push1("b")
        l.push1("c")
        l.push1("d")
        l.printme()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()