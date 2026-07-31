class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        MaxConsecutive = 0
        Consecutive = 0
        for i in range(len(nums)):
            if i == 0:
                if nums[i] == 1:
                    Consecutive = 1
                else:
                    pass
            elif nums[i] == 1:
                if nums[i] == nums[i-1]:
                    Consecutive +=1
                else:
                    Consecutive = 1
            elif nums[i] == 0:
                Consecutive = 0
            if Consecutive > MaxConsecutive:
                MaxConsecutive = Consecutive
        return MaxConsecutive
