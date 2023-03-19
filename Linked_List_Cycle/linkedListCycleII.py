# Time Complexity : O(n) 
# Space Complexity : O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #edge case
        if not head:
            return head

        slow = head
        fast = head
        cycle = False

        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next

            if slow==fast:
                cycle=True
                break


        if not cycle:
            return None

        slow = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next

        return slow