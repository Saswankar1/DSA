class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Initialize the write index to 1, as the first element is always unique
        write_index = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                # Assign the current unique element to the write index
                nums[write_index] = nums[i]
                # Move the write index forward
                write_index += 1
        
        return write_index
