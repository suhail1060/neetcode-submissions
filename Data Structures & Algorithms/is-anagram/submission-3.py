class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not(len(s)==len(t)):
            return False
        dicts={}
        dictt={}
        for char in s:
            if char in dicts:
                dicts[char]+=1
            else : 
                dicts[char]=1
        
        for char in t:
            if char in dictt:
                dictt[char]+=1
            else:
                dictt[char]=1
        print(dicts, dictt)
        for key in dicts:
            if not( key in dictt):
                return False
            elif not(dicts[key]==dictt[key]):
                return False
        return True
        