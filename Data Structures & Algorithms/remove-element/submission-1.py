class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = list()
        for num in nums:
            if num != val:
                k.append(num)
        return len(k)