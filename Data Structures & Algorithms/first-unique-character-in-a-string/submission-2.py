class Solution:
    def firstUniqChar(self, s: str) -> int:

        hashmap = {}


        for char in s:
            freq = hashmap.get(char, 0) + 1
            hashmap[char] = freq

        
        for item, val in hashmap.items():
            if hashmap[item] == 1:
                return s.index(item)
        return -1