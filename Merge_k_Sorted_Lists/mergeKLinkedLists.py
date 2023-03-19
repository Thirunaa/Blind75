# Time Complexity : O(n logk) 
# Space Complexity : O(k)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # override the less than (custom comparator) function for the listnode, to look into value of the nodes while comparing them 
        ListNode.__lt__ = lambda a,b : a.val<b.val

        minheap=[]
            
        result = ListNode(-1)
        curr = result

        for lhead in lists:
            if lhead:
                heappush(minheap,lhead)

        while minheap:
            top = heappop(minheap)
            curr.next = top
            curr = curr.next
            if top.next:
                heappush(minheap,top.next)


        return result.next
            