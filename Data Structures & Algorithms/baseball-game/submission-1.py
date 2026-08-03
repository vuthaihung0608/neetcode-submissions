class Solution:
    def calPoints(self, operations: List[str]) -> int:
        array = []
        index = 0
        for i in operations:
            if i == "D":
                array.append(int(array[index -1])*2)

            elif i == "C":
                array.pop()
                index -=2
            elif i == "+":
                array.append(int(array[index-1]) + int(array[index-2]))
            
            else:

                array.append(int(i))
            index +=1
        return sum(array)
