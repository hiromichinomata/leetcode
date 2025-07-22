class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        for _ in range(n):
            nums1.pop()
        result = []
        while i < len(nums1) and j < len(nums2):
            a = nums1[i]
            b = nums2[j]
            if a < b:
                result.append(a)
                i += 1
            else:
                result.append(b)
                j += 1
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        while j < len(nums2):
            result.append(nums2[j])
            j += 1

        for _ in range(len(nums1)):
            nums1.pop()
        for i in result:
            nums1.append(i)
