class Solution:
    def calPoints(self, operations: List[str]) -> int:
        array = []
        for i in operations:
            if i == "+":
                array.append(array[-1]+array[-2])
            elif i == "D":
                array.append(array[-1]*2)
            elif i == "C":
                array.pop()
            else:
                array.append(int(i))
        return sum(array)