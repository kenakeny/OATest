class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix=1
        for n in range(len(nums)):
            res[n]=prefix
            prefix*=nums[n]
        postfix=1
        for i in range (len(nums)-1, -1 ,-1) :
            # we now do postfix
            res[i]*=postfix
            postfix*=nums[i]
        return res
        #whoever thought about doing postfix and prefix instead of division is pretty smart ngl it was fun learning it, i didnt wanna put the divsion answer here