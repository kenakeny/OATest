class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #make a set so that u dont have dupe values we check if we have a value already present if we do we remove from the left until we reach this value that's present. we add new Val then we update MAXL
        mySet=set()
        l=0
        maxL=0
        for r in range(len(s)):
            while s[r] in mySet:
                mySet.remove(s[l]) 
                l += 1
            mySet.add(s[r])
            maxL=max(maxL,(r-l+1))
        return maxL