class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      for num in nums:
        if num == nums:
            return True
        else:
            return False
        