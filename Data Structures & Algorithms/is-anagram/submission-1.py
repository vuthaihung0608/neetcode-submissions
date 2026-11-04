class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = ''.join(sorted(s))
        t1 = ''.join(sorted(t))
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s1)):
                if s1[i] != t1[i]:
                    return False
            return True
            