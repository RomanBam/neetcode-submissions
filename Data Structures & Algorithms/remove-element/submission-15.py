class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        klist = []
        for num in nums:
            if num != val:
                klist.append(num)
        for i in range(len(klist)):
            nums[i] = klist[i]
        return len(klist)