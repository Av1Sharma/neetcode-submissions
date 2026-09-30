class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = {}
        for char in arr:
            result = hashmap.get(char, 0) + 1
            hashmap[char] = result

        res = []
        for keys, vals in hashmap.items():
            if vals == 1:
                res.append(keys)

        if k-1 >= len(res):
            return ""
        
        return res[k-1]