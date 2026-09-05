class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #o(n2)
        # # for (i=0;i<nums.length-2;i++):
        # for i in range(len(nums)-1):
        #     # for(j=i+1;j<nums.length;j++):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i]==nums[j]):
        #             return True
        # return False

        #Turns out the array is not sorted
        # if(len(nums)<2):
        #     return False
        # elif(nums[1]>nums[0] and not(nums[1]==nums[0])):
        #     for i in range(len(nums)-1):
        #         if not(nums[i+1]>nums[i]):
        #             return True
        # elif(nums[1]<nums[0] and not(nums[1]==nums[0])):
        #     for i in range(len(nums)-1):
        #         if not(nums[i+1]<nums[i]):
        #             return True
        # return False


        #Time limit exceeded
        # for i in range(len(nums)):
        #     if(nums.count(nums[i])>1):
        #         return True
        # return False

    #    first sort then check next
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if ((nums[i])==(nums[i+1])):
        #         return True
        # return False

        # array to set so duplicates will be removed then compare lenght of set and array
        # sett=set(nums);
        # if not(len(sett)==len(nums)):
        #     return True
        # return False

    # recommended solution
        # seen=set()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen.add(i)
        # return False

        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                return True
        return False