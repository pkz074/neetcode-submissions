class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        top = {} 

        for num in nums:
            
            top[num] = top.get(num, 0) + 1

        sorted_val = sorted(top, key=top.get, reverse=True)
        return sorted_val[:k]