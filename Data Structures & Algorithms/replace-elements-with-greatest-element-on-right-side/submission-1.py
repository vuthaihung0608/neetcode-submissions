class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        new_array = []
        max = -1
        for i in range(length):
            list_for_check = list(range(i+1,length))
            if list_for_check != []:
                for y in list_for_check:
                    if arr[y] > max:
                        max = arr[y]
                new_array.append(max)
                max = -1
            else:
                new_array.append(-1)
        return new_array
                
            