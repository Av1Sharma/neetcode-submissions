class Solution:
    def countSeniors(self, details: List[str]) -> int:
        index = -1
        count = 0

        for word in details:
            if word.find('M') > 0:
                index = word.find('M')
            else:
                index = word.find('F')
            
            if int(word[index+1: index+3]) > 60:
                count +=1
            
        return count
        
        

