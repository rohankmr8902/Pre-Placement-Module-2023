class Solution:
    def searchRange(self, nums, target):
        i=0
        l=len(nums)-1
        f,e=-1,-1
        while(i<=l):
            if(f<0):
                if(nums[i]==target):
                    f=i
            if(e<0):
                if(nums[l]==target):
                    e=l
            if(f>=0 and e>=0):
                break
            if(f<0):
                i+=1
            if(e<0):
                l-=1
        return [f,e]