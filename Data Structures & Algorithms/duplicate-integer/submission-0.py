class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stack = []
        for i in nums:
            if i in stack:
                return True
            stack.append(i)
        return False