class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_sorted = sorted(t)
        s_sorted = sorted(s)
        if s_sorted == t_sorted:
            return True
        return False