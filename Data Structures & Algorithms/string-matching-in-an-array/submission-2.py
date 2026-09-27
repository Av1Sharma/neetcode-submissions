class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        ## just going to brute force
        ## there is obv a better way, but not sure...

        ## Why I switched from array to set, 
        ## Set takes cares of duplicates automatically

        ## this is a terrible solution though

        ## lets see what i should've done

        ## what the fuck.

        ## wait didn't I do this and get it wrong??

        seen = set()
        for i in range(len(words)):
            for j in range(0, len(words)):

                if j==i:
                    continue

                if words[i] in words[j]:
                    seen.add(words[i])
        return list(seen)

        