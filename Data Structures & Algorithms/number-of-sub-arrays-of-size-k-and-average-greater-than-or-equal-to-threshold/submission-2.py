class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        wTotal = 0
        for i in range(k):
            wTotal += arr[i]
        res = 0
        left = 0
        if wTotal / k >= threshold:
            res += 1
        for r in range(k, len(arr)):
            
            wTotal += arr[r]
            wTotal -= arr[left]
            left +=1
            if (wTotal / k) >= threshold:
                res +=1
        return res

