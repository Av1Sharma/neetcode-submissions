class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        numOfPairs = len(nums) // 2

        hash1 = {}

        for num in nums:
            result = hash1.get(num, 0) + 1
            hash1[num] = result


        pairs = 0
        for key, vals in hash1.items():
            if vals == 2:
                pairs +=1
            if vals > 2:
                while vals >= 2:
                    vals = vals - 2
                    pairs +=1
            print(pairs)
        return pairs == numOfPairs


        