class Solution:
    def countSeniors(self, details: List[str]) -> int:
        index = -1
        count = 0

        for word in details:
            if word.find('M') > 0:
                index = word.find('M')
            elif word.find('F') > 0:
                index = word.find('F')
            else:
                continue
                
            
            if int(word[index+1: index+3]) > 60:
                count +=1
            
        return count
        
        

