import unittest
import problems

class TestCorrectness(unittest.TestCase):

    def test_easy_712_1(self):
        self.assertTrue(problems.easy_712.solve_easy_712('()'))
    def test_easy_712_2(self):
        self.assertTrue(problems.easy_712.solve_easy_712('([])'))
    def test_easy_712_3(self):
        self.assertTrue(problems.easy_712.solve_easy_712('{([])}'))
    def test_easy_712_4(self):
        self.assertFalse(problems.easy_712.solve_easy_712('{([])})'))
    def test_easy_712_5(self):
        self.assertTrue(problems.easy_712.solve_easy_712('{}{}'))
    def test_easy_712_6(self):
        self.assertTrue(problems.easy_712.solve_easy_712('[{}{}]'))
    def test_easy_712_7(self):
        self.assertTrue(problems.easy_712.solve_easy_712('[{}{}]([])'))
    def test_easy_712_7(self):
        self.assertFalse(problems.easy_712.solve_easy_712('[{}{}]([{])'))

if __name__ == '__main__':
    unittest.main()