class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            max1 = -1000000
            for j in range(i+1, len(arr)):
                max1 = max(max1, arr[j])
            arr[i] = max1

        arr[len(arr)-1] = -1

        return arr
        