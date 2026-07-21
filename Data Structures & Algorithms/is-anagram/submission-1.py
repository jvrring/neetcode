from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two strings must be same length
        if len(s) != len(t):
            return False

        # im not making my own hash tables
        s_count = Counter(s)
        t_count = Counter(t)

        for i in s_count:
            if s_count[i] != t_count[i]:
                return False
            
        return True