# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        arr = []
        node = head
        while True:
            arr.append(node)
            if node.next is None:
                break
            node = node.next
        arr.reverse()
        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i].next = None
                break
            node0 = arr[i]
            node1 = arr[i+1]
            node0.next = node1
        return arr[0]
