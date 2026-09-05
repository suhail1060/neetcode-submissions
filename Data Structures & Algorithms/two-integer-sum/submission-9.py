class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        # d=nums.copy()
        # d.sort()
        # i=0
        # j=len(nums)-1
        # v1=-1
        # v2=-1
        # while i<j:
        #     if d[i]+d[j]==target:
        #         v1=d[i]
        #         v2=d[j]
        #         break
        #     elif d[i]+d[j]>target:
        #         j-=1
        #     else:
        #         i+=1
        # # ans=[nums.index(v1),nums.index(v2)]
        # # ans.sort()
        # # return ans
        # ans=[]
        # # print(nums, d)
        # for i in range(len(nums)):
        #     if(nums[i]==v1 or nums[i]==v2):
        #         ans.append(i)
        #     elif len(ans)==2:
        #         break
        # return ans;

        A=[]
        for i,val in enumerate(nums):
            A.append([val, i])
        A.sort()
        i=0
        j=len(A)-1
    
        while i<j:
            if(A[i][0]+A[j][0]==target):
                return [min(A[i][1], A[j][1]), max(A[i][1],A[j][1])]
            elif (A[i][0]+A[j][0]<target):
                i+=1
            else:
                j-=1