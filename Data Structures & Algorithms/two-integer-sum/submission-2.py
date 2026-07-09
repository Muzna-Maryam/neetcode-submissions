class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hashmap:
                # return [i, hashmap[diff]] not correct bcz 
                # have to return the smaller index first so
                return [hashmap[diff], i] 
                # fixes bcz i is current index and the 
                # hashmap[diff] < i, always
            hashmap[n] = i # else add to hashmap  
        
        return []
        