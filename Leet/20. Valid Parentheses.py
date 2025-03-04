# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_dict = {')':'(','}':'{',']':'['}
        stack = []
        for char in s:
            if char in valid_dict:
                if stack and stack[-1] == valid_dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
sol = Solution()
print(sol.isValid("]"))