# Time Complexity : O(n) 
# Space Complexity : O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head

        while current !=None:
            temp = current.next
            current.next = prev

            #reset previous and current pointer for next iteration
            prev = current
            current = temp

            #current.next,prev,current = prev,current, current.next

        return prev