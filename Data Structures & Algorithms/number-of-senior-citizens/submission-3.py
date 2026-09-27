class Solution:
    def countSeniors(self, details: List[str]) -> int:

        count = 0
        for p in details:
            if p.find('M') == -1:
                index = p.find('F')
            if p.find('F') == -1:
                index = p.find('M')
            
            age = p[index+1: index+3]
            if int(age) > 60:
                count +=1
            

        return count