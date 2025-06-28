#learning python just for this position LOL INSHALLAH EVERYTHIGN GOES WELL
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenSet=set()        
        for num in nums:
            if num in seenSet:
                return True
            seenSet.add(num)
        return False
# we could also just use python being fun and make a set of this list automatically and compare lengthssss!!
