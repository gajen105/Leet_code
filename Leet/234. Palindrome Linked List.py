# Given the head of a singly linked list, return true if it is a 
# palindrome
#  or false otherwise.

#  Input: head = [1,2,2,1]
# Output: true

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev= slow
            slow = next_node
        left = head
        right = prev
        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True
