from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        arr = []
        map_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            map_dict[key].append(s)
    
        return list(map_dict.values())