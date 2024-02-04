"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    List solution

    """
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # curr_node = head
        nodes = []

        while head:
            nodes.append(head)
            head = head.next

        if len(nodes) <= 1:
            return None

        i = len(nodes) - n

        if i == 0:
            return nodes[i + 1]
        else:
            nodes[i - 1].next = nodes[i - 1].next.next
            return nodes[0]


if __name__ == '__main__':
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = Solution().removeNthFromEnd(node, 2)
    while result:
        print(result.val)
        result = result.next

    node = ListNode(1, None)
    result = Solution().removeNthFromEnd(node, 1)
    assert result is None
