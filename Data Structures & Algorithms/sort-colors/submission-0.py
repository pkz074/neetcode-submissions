class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = defaultdict(int)

        minval, maxval = min(nums), max(nums)

        for val in nums:
            count[val] += 1
        
        index = 0
        for val in range(minval, maxval+1):
            while count[val] > 0:
                nums[index] = val
                index += 1
                count[val] -=1

    print(sortColors)