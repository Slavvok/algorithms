"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that
the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""


class Solution:
    """
    Recursion solution
    34 ms, Beats 77 %
    """
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        num_dict = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": ""
        }

        dig_to_str = []

        for i in digits:
            dig_to_str.append(num_dict[i])

        output = self._product(dig_to_str)

        return ["".join(i) for i in output]

    def _product(self, ar_list):
        if not ar_list:
            yield ()
        else:
            for a in ar_list[0]:
                for prod in self._product(ar_list[1:]):
                    yield (a,) + prod


if __name__ == '__main__':
    digits = "23"
    result = Solution().letterCombinations(digits)
    assert result == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    digits = "234"
    result = Solution().letterCombinations(digits)
    assert result == ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh',
                      'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
