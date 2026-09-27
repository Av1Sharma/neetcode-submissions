class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hmap = {}


        for num in nums:
            result = hmap.get(num, 0) + 1  
            hmap[num] = result

        sorted_elements = sorted(hmap.keys(), key=hmap.get, reverse=True)

        # 3. Slice the list to return the top K elements
        return sorted_elements[:k]


           



        