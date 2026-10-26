class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            alphabet = [0] * 26
            for letter in word:
                score = ord(letter) - ord('a')

                alphabet[score] +=1


            key = tuple(alphabet)


            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(word)


        return list(hashmap.values())

                
        