class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
        j, maxx, res = 0, 0, 0


        count = {}

        for i in range(len(s)):

            count[s[i]] = count.get(s[i], 0) + 1

            maxx = max(maxx, count[s[i]])

            while (i - j + 1) - maxx > k:

                count[s[j]] -=1
                j+=1

            res = max(res, i - j + 1)
        return res