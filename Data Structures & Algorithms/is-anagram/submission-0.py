class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # a=sorted(s)
        # b=sorted(t)
        if (sorted(s)==sorted(t)):
            return True
        return False
        
        