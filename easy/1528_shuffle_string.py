class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        pair = []
        for i in range(len(s)):
            pair.append([s[i], indices[i]])
        sorted_pair = sorted(pair, key=lambda x: x[1])
        result = []
        for i in sorted_pair:
            result.append(i[0])
        return ''.join(result)
