# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #main priority becomes the bifurcation of the list / splitiing the list into two parts
        #we can use a slow and a fast pointer for that

        slow = head
        fast = head.next

        #we used fast and fast.next because given the number of elements, it might be fast or fast.next which reaches the end of the list to NULL first
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        #now we begin the reversal of the second list

        second = slow.next
        prev = None
        slow.next = None

        while second:
            tmp = second.next #preserving chain
            second.next = prev #making first as last , essentially reversing
            prev = second
            second = tmp

        
        first = head
        second = prev
        #merging the two lists together
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
    

        