import unittest
from problems import easy_712, easy_714, easy_825, easy_832
from commonss import linked_list as ll
class TestCorrectness(unittest.TestCase):

    def test_easy_712_1(self):
        self.assertTrue(easy_712.solve_easy_712('()'))
    def test_easy_712_2(self):
        self.assertTrue(easy_712.solve_easy_712('([])'))
    def test_easy_712_3(self):
        self.assertTrue(easy_712.solve_easy_712('{([])}'))
    def test_easy_712_4(self):
        self.assertFalse(easy_712.solve_easy_712('{([])})'))
    def test_easy_712_5(self):
        self.assertTrue(easy_712.solve_easy_712('{}{}'))
    def test_easy_712_6(self):
        self.assertTrue(easy_712.solve_easy_712('[{}{}]'))
    def test_easy_712_7(self):
        self.assertTrue(easy_712.solve_easy_712('[{}{}]([])'))
    def test_easy_712_7(self):
        self.assertFalse(easy_712.solve_easy_712('[{}{}]([{])'))
    # def test_easy_714_1(self):
    #     l = ll.LinkedList()
    #     l.push1("a")
    #     l.push1("b")
    #     l.push1("c")
    #     l.push1("d")
    #     h = easy_714.solve_easy_714(l.head)
    #     self.assertEqual(get_concatinated_list(h),'badc')
    def test_easy_832_1(self):
        actual_ans = [3, 8, 2, 5, 9]
        solved_arry = easy_832.solve_easy_832([3, 8, 2, 5, 9, 5, 1, 4])
        self.assertTrue(actual_ans == solved_arry)

    def test_easy_832_2(self):
        actual_ans = [5, 2, 3, 4, 1]
        solved_arry = easy_832.solve_easy_832([5, 1, 3, 5, 2, 3, 4, 1])
        self.assertTrue(actual_ans == solved_arry)

    def test_easy_832_3(self):
        actual_ans = [1, 3, 5, 2]
        solved_arry = easy_832.solve_easy_832([5, 1, 3, 5, 2, 5, 4, 5])
        self.assertTrue(actual_ans == solved_arry)

    def test_easy_825_1(self):
        actual_ans = [0, 4, 4, 9, 81]
        solved_arr = easy_825.solve_easy_825([-9, -2, 0, 2, 3])
        self.assertTrue(actual_ans == solved_arr)

    def test_easy_825_2(self):
        actual_ans = [0, 4, 4, 9, 49, 81,100]
        solved_arr = easy_825.solve_easy_825([-10, -9, -7, -2, 0, 2, 3])
        self.assertTrue(actual_ans == solved_arr)


def get_concatinated_list(head):
        temp = head
        o = ''
        while(temp):
            o = o + temp.data
            temp = temp.next
        return o

if __name__ == '__main__':
    unittest.main()