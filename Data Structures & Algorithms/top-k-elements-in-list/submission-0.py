class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we count the frequencies, normal hashmap 
        # so basically count is givng us:
        # count = {1: 1, 2: 2, 3: 3}
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # freq is the list of buckets 
        # Job: flip the tally sheet around. 
        # Instead of "number → its frequency," organize it 
        # as "frequency → which numbers have it." 
        # This is what lets us skip sorting.
        freq = [[] for i in range(len(nums) + 1)]

        # So when you write freq[c].append(n), you're saying: 
        # "the number n has frequency c, so drop n into the 
        # bucket at index c."
        for n, c in count.items():
            freq[c].append(n)

        # now simce we are moving from top 
        # to down in the freq we dont have to 
        # sort and get the n appearing most times (k) 
        # first and add it to the res 
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res           


