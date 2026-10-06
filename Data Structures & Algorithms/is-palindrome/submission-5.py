class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = s[::-1]
        return ss