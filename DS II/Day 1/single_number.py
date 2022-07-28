class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
       
        for p, num in enumerate(nums):
           
            if nums[p] in s:
                
                s.remove(nums[p])
               
            else:
                s.add(nums[p])
        
        s = list(set(s))
       
        return s[0]