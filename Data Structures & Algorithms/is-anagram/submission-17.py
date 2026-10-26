class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}


        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        
        for char in t:
            if char not in hashmap:
                return False
            else:
                hashmap[char] -=1
        
        for value in hashmap.values():
            if value < 0 or value > 0:
                return False
        return True
        