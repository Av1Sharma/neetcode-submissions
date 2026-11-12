class Solution:
    def minOperations(self, logs: List[str]) -> int:
        keys = {
            "../" : -1,
            "./" : 0, 
            '/' : 1
        }
        count = 0
        for item in logs:
            if "../" in item or "./" in item:
                count += keys[item]
                if "../" in item and count < 0:
                    count +=1
            else:
                count +=1
        
        return max(0, count)