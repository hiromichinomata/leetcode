# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        hv = head.val
        hn = head.next

        if hn is None:
            return head

        nv = hn.val
        nn = hn.next
        hn.next = head
        if nn is None:
            head.next = None
        else:
            head.next = self.swapPairs(nn)
        return hn
