class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t.sort()
        s.sort()
        if s == t:
            return False
        return True