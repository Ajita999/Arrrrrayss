def twoSums(nums, target):
        for i in range(0,len(nums)):
          comp = target-nums[i]
          if(comp in nums[i+1:]):
            return [i,(nums[i+1:].index(comp)+i+1)]
        return[None,None]

print(twoSums([1,2,3,0,3,9],6))