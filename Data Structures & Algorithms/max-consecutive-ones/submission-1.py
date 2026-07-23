class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        summ = 0
        sure = 0
        for num in nums:
            if num == 1:
                summ += 1
            else:
                if sure < summ: sure = summ
                summ = 0
        return max(sure, summ)