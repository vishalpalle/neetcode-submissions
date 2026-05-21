class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ls = []
        for num in nums:
            if num in ls:
                return True
            ls.append(num)

        return False