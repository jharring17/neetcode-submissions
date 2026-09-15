class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars = list(s)
        t_chars = list(t)
        s_chars.sort()
        t_chars.sort()
        for i in range(0, len(s), 1):
            if s_chars[i] != t_chars[i]:
                return False
        return True