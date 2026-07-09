# this sol uses sorting 

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hashmap = defaultdict(list)

#         for word in strs:
#             key = "".join(sorted(word))
#             hashmap[key].append(word)
        
#         return list(hashmap.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        # not hashmap = {} because the one we used 
        # makes sure that hashmap already has a list created

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1
                #ord is basically ASCII so we are 
                #subtracting the ASCII of this char 
                # with that of a (97) bcz smaller letter in 
                # all 26 and then increment with one like 
                # finds the index and makes it 1 from 0
                # so eg: (c-a) 99 - 97 = 2
                # count[2] += 1
                # [1,0,1,0,...]

            hashmap[tuple(count)].append(word)
            # if we only did count it would be []
            # tuple count makes it (), list cant be key 
            # tuple is hashable 
            # so basically count is key and word is value 
            # { (1,0,1,0,...,1,...): ["act"] }


        return list(hashmap.values())
        # hashmap.values() groups them and then the list 
        # converts it to a list as required 




