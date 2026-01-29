class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i != j:
                    break
            else:
                return nums[i]  