class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        array = nums
        length= len(array)
        for i in range(length):
            for num in nums:
                array.append(num)
        return array