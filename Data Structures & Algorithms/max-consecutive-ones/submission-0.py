class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, count = 0, 0
        for num in nums:
            if num == 0:
                count = 0
                res = max(res,count)
            else:
                count += 1
        return max(res,count)