class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not(len(s)==len(t)):
            return False
        s="".join(sorted(s))
        t="".join(sorted(t))
        for i in range(len(s)):
            if not(s[i]==t[i]):
                return False
        return True

