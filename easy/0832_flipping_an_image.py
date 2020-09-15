class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        arr1 = []
        for i in A:
            arr1.append(i[::-1])
        result = []
        for i in arr1:
            tmp = []
            for j in i:
                if j == 1:
                    tmp.append(0)
                else:
                    tmp.append(1)
            result.append(tmp)
        return result
