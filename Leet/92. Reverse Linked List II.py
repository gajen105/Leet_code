# Given the head of a singly linked list and two integers left and right where left <= right, 
# reverse the nodes of the list from position left to position right, and return the reversed list.
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode
        """
        ans = ListNode(-1,head)
        left_node = ans
        for _ in range(left-1):
            left_node = left_node.next
        prev = left_node
        right_node = left_node.next
        for _ in range(right-left+1):
            temp = right_node
            right_node = right_node.next
            temp.next = prev
            prev = temp
        left_node.next.next = right_node
        left_node.next = prev
        return ans.next