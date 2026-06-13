class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:

        hashset = set()
        nums.sort()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False