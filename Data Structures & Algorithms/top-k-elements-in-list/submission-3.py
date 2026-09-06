class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=1+d.get(i, 0)
        heap=[]
        for j in d.keys():
            heapq.heappush(heap,(d[j], j))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for l in range(k):
            res.append(heapq.heappop(heap)[1])
        return res