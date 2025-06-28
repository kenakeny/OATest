class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: #type:ignore
        l,r=0 ,len(numbers)-1 #this is pretty simple two pointers question, left pointer from start and right ptr from end
        while l<r:
            cS= numbers[l] + numbers[r]
            if cS>target: #if currentSum is bigger than target, R is too big, we decrease R
                r-=1
            elif cS<target: #what if CurrentSum is smaller, we can increase L
                l+=1
            else:
                return [l+1,r+1] #equal indices r found

        return []