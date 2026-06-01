class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        seen = set()
        i, j = 0, 0
        maxx = 0

        while i < len(s):
            c = s[i]

            while c in seen:
                seen.remove(s[j])
                j+=1
            seen.add(c)
            #[1,2,3,4,1]
            #[j.....i]
            #[i(3) - j(0) = 3 which is wrong so]
            # we do "i - j + 1" so we calculate the bounds
            maxx = max(maxx, i-j+1)
            i+=1
        return maxx

        