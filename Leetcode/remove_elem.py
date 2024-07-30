class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Index to place the next non-val element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# Example usage:
nums1 = [3, 2, 2, 3]
val1 = 3
solution = Solution()
k1 = solution.removeElement(nums1, val1)
print(k1)  # Output: 2
print(nums1[:k1])  # Output: [2, 2]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
k2 = solution.removeElement(nums2, val2)
print(k2)  # Output: 5
print(nums2[:k2])  # Output: [0, 1, 3, 0, 4]
