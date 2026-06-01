class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5#hello
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    5#hello, 6#mayber = [hello, mayber]
    """
    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) #de 0 até #
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res