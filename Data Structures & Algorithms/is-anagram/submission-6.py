class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #o(n+n+n)
        # if not(len(s)==len(t)):
        #     return False
        # dicts={}
        # dictt={}
        # for char in s:
        #     if char in dicts:
        #         dicts[char]+=1
        #     else : 
        #         dicts[char]=1
        
        # for char in t:
        #     if char in dictt:
        #         dictt[char]+=1
        #     else:
        #         dictt[char]=1
        # print(dicts, dictt)
        # for key in dicts:
        #     if not( key in dictt):
        #         return False
        #     elif not(dicts[key]==dictt[key]):
        #         return False
        # return True

        # if not(len(s)==len(t)):
        #     return False
        
        # sortedS=sorted(s)
        # sortedT=sorted(t)

        # for i in range(len(s)):
        #     if not(sortedS[i]==sortedT[i]):
        #         return False
        # return True
            

        # if len(s)!=len(t):
        #     return False
        # return sorted(s)==sorted(t)

        dictS={}
        dictT={}

        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if(s[i] in dictS):
                dictS[s[i]]+=1
            else:
                dictS[s[i]]=1
            if(t[i] in dictT):
                dictT[t[i]]+=1
            else:
                dictT[t[i]]=1
        # print(dictT, dictS)
        for key in dictS:
            if not(key in dictT):
                return False
            elif (dictS[key]!=dictT[key]):
                return False
        return True