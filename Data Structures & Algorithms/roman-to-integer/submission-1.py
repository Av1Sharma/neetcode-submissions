class Solution:
    def romanToInt(self, s: str) -> int:
       map1 = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
       }

       total = 0
       for i in range(len(s) - 1, -1, -1):
        if i == len(s) - 1:
            total += map1[s[i]]
            continue
        if map1[s[i]] < map1[s[i+1]]:
            total -=map1[s[i]]
        else:
            total +=map1[s[i]]
       return total
         