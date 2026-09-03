class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = []
        for num in nums:
            if num != val:
                k.append(num)
            else:
                return len(k)