class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        i, j, maxx = 0, 0, 0

        while i < len(s):

            c = s[i]

            while c in seen:

                seen.remove(s[j])
                j+=1
            seen.add(c)
            maxx = max(maxx, i-j+1)
            i+=1
        return maxx
    