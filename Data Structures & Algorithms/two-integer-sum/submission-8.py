class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # create dict
        seen = {}
        # create i (index), num (number) 
        #{0: 1, 1: 3, 2: 7, etc}
        #{0, 1, 2 = i}
        #{1, 3, 7 = num}
        for i, num in enumerate(nums):

        # nums[i] + nums[j] = target
        # nums[j] = target - nums[i]
            # 8 = 10 - 2
            diff = target - num

            if diff in seen:
                return [seen[diff], i]

            seen[num] = i
