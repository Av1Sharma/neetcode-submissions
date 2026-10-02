class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        left = 0
        res = 0

        for right in range(len(fruits)):

            # add incoming fruit
            count[fruits[right]] = count.get(fruits[right], 0) + 1

            # INVALID WINDOW: more than 2 fruit types
            while len(count) > 2:

                # remove outgoing fruit
                count[fruits[left]] -= 1

                if count[fruits[left]] == 0:
                    del count[fruits[left]]

                left += 1

            res = max(res, right - left + 1)

        return res

        