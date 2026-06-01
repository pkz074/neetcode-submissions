class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        out = [1] * n

        # divide array in before NUM and after

        preffix = 1
        for i in range(n):
            out[i] = preffix
            preffix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            out[i] *= suffix
            suffix *= nums[i]

        return out