class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def sorting():

            count = defaultdict(int)

            minval, maxval = min(nums), max(nums)

            for val in nums:
                count[val] += 1
            
            index = 0
            for val in range(minval, maxval+1):
                while count[val] > 0:
                    nums[index] = val
                    index += 1
                    count[val] -= 1

        sorting()
        return nums