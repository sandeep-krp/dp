import unittest
from problems import easy_712, easy_714, easy_818, easy_819, easy_821, easy_825, easy_832,leet_zigzag_conversion, leet_longest_substring_without_repeating_characters
from commonss import linked_list as ll
from data import data_1
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

    def test_easy_821_1(self):
        self.assertTrue(easy_821.solve_easy_821([-6, 0, 2, 40]) == 2)

    def test_easy_821_2(self):
        self.assertFalse(easy_821.solve_easy_821([1, 5, 7, 8]))

    def test_easy_819_1(self):
        self.assertTrue(easy_819.solve_819([9, 11, 8, 1, 7, 11]) == 10)

    def test_easy_819_2(self):
        self.assertTrue(easy_819.solve_819([11, 2, 10, 1, 10, 1]) == 9)

    def test_easy_819_3(self):
        self.assertTrue(easy_819.solve_819([11, 10, 9, 8, 7, 6]) == 0)

    def test_easy_819_4(self):
        self.assertTrue(easy_819.solve_819(data_1.data) == 3)

    def test_818_1(self):
        self.assertTrue(easy_818.solve_818(10) == [2, 3, 5, 7])

    def test_818_1(self):
        self.assertTrue(easy_818.solve_818(25) == [2, 3, 5, 7, 11, 13, 17, 19, 23])

    def test_leet_zigzag_conversion_1(self):
        self.assertTrue(leet_zigzag_conversion.solve_leet_zigzag_conversion('PAYPALISHIRING',3)=='PAHNAPLSIIGYIR')

    def test_leet_zigzag_conversion_2(self):
        self.assertTrue(leet_zigzag_conversion.solve_leet_zigzag_conversion('PAYPALISHIRING',4)=='PINALSIGYAHRPI')

    def test_leet_zigzag_conversion_3(self):
        self.assertTrue(leet_zigzag_conversion.solve_leet_zigzag_conversion('AB',1)=='AB')

    def leet_longest_substring_without_repeating_characters_1(self):
        self.assertTrue(leet_longest_substring_without_repeating_characters('abcabcbb') == 3)

    def leet_longest_substring_without_repeating_characters_2(self):
        self.assertTrue(leet_longest_substring_without_repeating_characters('abb') == 2)

    def leet_longest_substring_without_repeating_characters_3(self):
        self.assertTrue(leet_longest_substring_without_repeating_characters('') == 0)

def get_concatinated_list(head):
        temp = head
        o = ''
        while(temp):
            o = o + temp.data
            temp = temp.next
        return o

if __name__ == '__main__':
    unittest.main()