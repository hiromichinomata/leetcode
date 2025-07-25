from collections import defaultdict

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head

        if node is None:
            return False

        checked = defaultdict(int)
        while True:
            checked[node] += 1
            if checked[node] >= 2:
                return True
            node = node.next
            if node is None:
                break

        return False
