"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Recursion solution
    42 ms, beats 46%
    """
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        res = ListNode()
        self._merge(list1, list2, res)
        return res.next

    def _merge(self, l1, l2, res):
        if l1 is None and l2 is None:
            return res

        if not l1:
            res.next = l2
            return res
        elif not l2:
            res.next = l1
            return res
        elif l1 and l1.val <= l2.val:
            res.next = l1
            l1 = l1.next
        elif l2 and l2.val < l1.val:
            res.next = l2
            l2 = l2.next

        res = res.next

        return self._merge(l1, l2, res)


if __name__ == '__main__':
    node1 = ListNode(1, ListNode(2, ListNode(4)))
    node2 = ListNode(1, ListNode(3, ListNode(4)))
    result = Solution().mergeTwoLists(node1, node2)
    while result:
        print(result.val)
        result = result.next

    node1 = None
    node2 = ListNode()
    result = Solution().mergeTwoLists(node1, node2)
    while result:
        print(result.val)
        result = result.next

    node1 = None
    node2 = None
    result = Solution().mergeTwoLists(node1, node2)
    print(result)
