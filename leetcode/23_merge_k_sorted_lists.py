# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1 or len(lists) == 1 and lists[0].val is None:
            return ListNode()
        unpacked = [self._unpack(i) for i in lists]
        res = []
        for i in unpacked:
            min = 0
            for j in i:
                if j <= min:
                    res.append(j)
        res = self._pack(res)
        return res


    def _unpack(self, node: ListNode):
        result = []
        while True:
            result.append(node.val)
            if node.next is None:
                break
            node = node.next
        return result

    def _pack(self, lists: list):
        ln = ListNode()
        for i in lists:
            ln.next = ListNode(val=i)
            ln = ln.next

        return ln


class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = len(lists)
        if len(lists) == 0 or lists is None:
            return None

        def merge_2_linkedlist(l1, l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val > l2.val:
                    tail.next = l2
                    l2 = l2.next
                else:
                    tail.next = l1
                    l1 = l1.next
                tail = tail.next

            while l1:
                tail.next = l1
                l1 = l1.next
                tail = tail.next

            while l2:
                tail.next = l2
                l2 = l2.next
                tail = tail.next

            return dummy.next

        while len(lists) > 1:
            answer = []
            for i in range(0, len(lists), 2):
                left_arr = lists[i]
                if i + 1 < len(lists):
                    right_arr = lists[i + 1]
                else:
                    right_arr = None

                answer.append(merge_2_linkedlist(left_arr, right_arr))
            lists = answer
        return lists[0]

"""
There should be dictionary containing all the numbers.
Upon iterating all LN several times we are appending each number to corresponding key in dict.
Then we are unpacking all values from dict and store them in LN starting from the end.
"""
