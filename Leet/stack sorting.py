class Solution:
    def stackSort(self, stack):
        if not stack:
            return stack
        sorted_stack = []
        while stack:
            temp = stack.pop()
            while sorted_stack and sorted_stack[-1] > temp:
                stack.append(sorted_stack.pop())
            sorted_stack.append(temp)
        return sorted_stack

sol = Solution()
stack = [6,3, 2, 1, 4, 5]
print(sol.stackSort(stack))  # [1, 2, 3, 4, 5]