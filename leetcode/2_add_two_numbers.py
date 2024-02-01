"""

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, ll1, ll2):
        number1 = Solution.from_linked_list(ll1)
        number2 = Solution.from_linked_list(ll2)
        result = number1 + number2
        result = Solution.to_linked_list([i for i in str(result)])
        return result

    @staticmethod
    def from_linked_list(lst) -> int:
        res = []
        curr = lst
        while True:
            res.append(curr.val)
            if curr.next is None:
                break
            curr = curr.next
        return int(''.join([str(i) for i in reversed(res)]))

    @staticmethod
    def to_linked_list(lst):
        ln = ListNode(val=lst[0], next=None)
        for i in range(1, len(lst)):
            curr = ListNode(val=lst[i], next=ln)
            ln = curr
        return ln


class Solution1:
    def add_two_numbers(self, ll1: ListNode, ll2: ListNode) -> ListNode:
        remain = 0
        result = ListNode(0)
        pointer = result
        while ll1.next or ll2.next or remain:
            last_num1 = ll1.val or 0
            last_num2 = ll2.val or 0
            last_sum = last_num1 + last_num2

            summ = last_sum % 10 + remain
            remain = last_sum // 10

            pointer.next = ListNode(summ)
            pointer = pointer.next

            ll1 = ll1.next
            ll2 = ll2.next

        return result.next


def show_result(ln: ListNode):
    curr = ln
    while True:
        print(curr.val)
        if curr.next is None:
            break
        curr = curr.next


if __name__ == "__main__":
    ln1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    ln2 = ListNode(4, ListNode(3, ListNode(2, ListNode(1))))

    result1 = Solution().add_two_numbers(ln1, ln2)
    show_result(result1)

    result2 = Solution1().add_two_numbers(ln1, ln2)
    show_result(result2)
