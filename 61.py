# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        ln = 0
        p3 = head
        while p3:
            ln+=1
            p3 = p3.next
        
        if not head or not head.next or ln == 0 or k % ln == 0:
            return head
        
        k = k % ln
        p1 = p2 = head
            
        for _ in range(k):
            p2 = p2.next
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        head, p2.next = p1.next, head
        p1.next = None
        
        # print(head.val, p2.val, p1.val)
        # pointer = head
        # while pointer.next:
        #     print(pointer.val)
        #     pointer = pointer.next
        return head
        