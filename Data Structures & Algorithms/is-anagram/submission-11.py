class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not(len(s)==len(t)):
            return False
        count=[0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')]+=1
            count[ord(t[i])-ord('a')]-=1
        for j in count:
            if not(j==0):
                return False
        return True
        