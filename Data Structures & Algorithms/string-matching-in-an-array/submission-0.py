class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        ## just going to brute force
        ## there is obv a better way, but not sure...

        output = []
        for i in range(len(words)):
            print(words[i])
            for j in range(0, len(words)):

                if j==i:
                    continue

                if words[i] in words[j]:
                    output.append(words[i])
        return output

        