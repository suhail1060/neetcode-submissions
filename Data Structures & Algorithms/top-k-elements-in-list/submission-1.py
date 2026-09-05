class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        desc={k: v for k, v in sorted(d.items(), key=lambda item:item[1] , reverse=True)}
        ans=[]
        for key,value in desc.items():
            if k==0:
                break
            else:
                k-=1
                ans.append(key)
        return ans

