class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l<=r:

            mid = l + ((r-l) // 2)
            #i.e r = 5, l = 3
            # 5 - 3 = 2 // 2 = 1 + 3 = 4
            # and indeed 4 is in the middle

            if nums[mid] > target:
                r = mid - 1
            
            elif nums[mid] < target:
                l = mid + 1

            else: return mid

        return -1