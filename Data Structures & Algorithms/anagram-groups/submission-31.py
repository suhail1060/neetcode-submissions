class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in range(0, len(strs)):
            a=strs[i]
            b="".join(sorted(strs[i]))
            if b in d:
                d[b].append(a)
            else:
                d[b]=[a]
        return list(d.values())

