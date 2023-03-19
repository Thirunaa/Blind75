# Time Complexity : O(n) 
# Space Complexity : O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        fast = head
        

        while n:
            if fast.next != None:
                fast = fast.next
                n-=1
            else:
                return head.next


        while fast.next != None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next


        return head