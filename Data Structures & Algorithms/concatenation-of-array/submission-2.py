class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        array = nums
        length= len(nums)
        for i in range(length):
            array.append(array[i])
        return array