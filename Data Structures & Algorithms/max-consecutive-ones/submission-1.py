class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = 0
        max_consecutive = 0
        for i in nums:
            if i == 1:
                consecutive +=1
            else:
                consecutive =0
            if max_consecutive < consecutive:
                max_consecutive = consecutive
        return max_consecutive