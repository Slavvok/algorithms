"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Iterative solution
    35 ms, beats 67 %
    """
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head

        out = first = ListNode(next=head)

        while first.next:
            middle = first.next
            last = middle.next

            if not first or not middle or not last:
                break
            middle.next, last.next = last.next, middle
            first.next, first = last, middle

        return out.next
        # left, right = head, head.next
        # head = right
        # while right:
        #     left.next, right.next = right.next, left
        #     if left.next:
        #         right, left = left.next.next, left.next
        #     else:
        #         break
        # return head


if __name__ == '__main__':
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    result = Solution().swapPairs(node)
    while result:
        print(result.val)
        result = result.next
    print("\n")

    node = ListNode(1, ListNode(2, ListNode(3)))
    result = Solution().swapPairs(node)
    while result:
        print(result.val)
        result = result.next
    print("\n")

    node = ListNode(1, ListNode(2))
    result = Solution().swapPairs(node)
    while result:
        print(result.val)
        result = result.next
    print("\n")
