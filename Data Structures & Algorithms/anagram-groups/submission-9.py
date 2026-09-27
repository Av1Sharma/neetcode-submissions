class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash1 = {}


        for word in strs:
            letters = [0] * 26

            for char in word:
                index = ord(char) - ord('a')

                letters[index] +=1

            key = tuple(letters)


            if key not in hash1:
                hash1[key] = []
            
            hash1[key].append(word)
        
        return list(hash1.values())
