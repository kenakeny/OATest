class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #here we wanna search for target- val
        #basically we make here a map that holds the vals we already passed
        #unironically this took me a longer time than usual, i struggled with one intend before the for loop :facepalm:
        x_map = {}
        for i, num in enumerate(nums):
         t = target - num
         if t in x_map:
            return [x_map[t], i]
         x_map[num] = i

    