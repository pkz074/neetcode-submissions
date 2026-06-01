class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = set()
        
        for num in nums:
            seen.add(num)
        
        if len(nums) != len(seen):
            return True

        return False
        