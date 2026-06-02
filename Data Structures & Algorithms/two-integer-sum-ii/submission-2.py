class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output=[]
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if j==i:
                    continue
                if numbers[i]+numbers[j]==target:
                    output.append(i+1)
                    output.append(j+1)
                    return output
        
                

        