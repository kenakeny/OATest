#basically we check for length first. if length is not equal we return false after that we make a counter for all characters seen :shrug: ezpz
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
         
        counterS, counterT= {},{}
        for i in range(len(s)):
            counterS[s[i]]=1+counterS.get(s[i],0)
            counterT[t[i]]=1+counterT.get(t[i],0)
        return counterS==counterT