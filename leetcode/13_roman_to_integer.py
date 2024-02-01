class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) < 1:
            return 0

        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        first_letter = {
            "I": I,
            "V": I,
            "X": X,
            "L": X,
            "C": C,
            "D": C,
            "M": M
        }
        whole = ""
        curr_value = ""
        output = []
        curr_position = None

        for i in range(len(s)-1):
            if not curr_position:
                curr_position = first_letter[s[i]]
            whole += s[i]
            print(whole)
            # if whole:
            # is_value = curr_position.index(whole)
            if whole + s[i+1] not in curr_position:
                output.append(curr_position.index(whole))
                whole = ""
                curr_position = first_letter[s[i+1]]
            if i == len(s) - 2:
                output.append(curr_position.index(whole + s[i+1]))
        print(output)

        return int("".join(str(i) for i in output))


class Solution2():
    def romanToInt(self, s):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total + roman[s[-1]]


if __name__ == '__main__':
    result = Solution().romanToInt("CCXXXIVC")
    print(result)
