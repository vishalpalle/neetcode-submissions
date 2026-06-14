class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                if nums[i] + nums[j] == target:
                    ind.append(i)
                    ind.append(j)
                    return ind