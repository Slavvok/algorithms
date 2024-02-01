"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest.
Sort the words with the same frequency by their lexicographical order.
"""


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        d = dict()

        for word in words:
            if not d.get(word):
                d[word] = 1
            else:
                d[word] += 1

        items = d.items()
        sorted(items, key=lambda x: x[1])
        return [i[0] for i in items][:k]


if __name__ == '__main__':
    wrds = ["i", "love", "leetcode", "i", "love", "coding"]
    result = Solution().topKFrequent(wrds, 2)
    print(result)
