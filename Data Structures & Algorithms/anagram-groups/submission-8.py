class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}

        for word in strs:
            arr = [0] * 26
            for char in word:
                result = ord(char) - ord('a')
                arr[result] +=1
            
            key = tuple(arr)


            if key in hmap:
                hmap[key].append(word)
            else:
                hmap[key] = []
                hmap[key].append(word)


        return list(hmap.values())
            
        