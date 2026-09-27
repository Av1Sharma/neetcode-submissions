class Solution:
    def findLucky(self, arr: List[int]) -> int:

        hash1 = {}


        for i in range(len(arr)):
            result = hash1.get(arr[i], 0) + 1

            hash1[arr[i]] = result
        lucky = -1
        for key, vals in hash1.items():
            if key == vals:
                lucky = key
        return lucky
        