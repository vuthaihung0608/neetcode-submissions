class Solution:
    def calPoints(self, operations: List[str]) -> int:
        array = []
        for i in operations:
            if i == "D":
                array.append(int(array[-1])*2)

            elif i == "C":
                array.pop()
            elif i == "+":
                array.append(int(array[-1]) + int(array[-2]))
            
            else:

                array.append(int(i))
        return sum(array)
