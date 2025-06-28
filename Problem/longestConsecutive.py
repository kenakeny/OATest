class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberSet=set(nums)
        if not numberSet:
            return 0
        longest =0
        for num in numberSet:
            if(num-1) not in numberSet:
                length=1
                while(num+length) in numberSet:
                    length+=1
                    longest=max(longest,length)
        if longest==0: longest+=1
        return longest
        #essentially you make a set for o(1) look up time then we iterate over the set, if this number-1 exists that means we can have an even longer consecutive sequeunce
        # so for example [ 1,2,0,4,3] if we start at 1 we're actually missing an even longer one which is 1-1 AKA starting at zero!!
        #lol i had to hard code in those two conditions
        