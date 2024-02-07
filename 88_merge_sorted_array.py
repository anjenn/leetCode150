# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Begin by setting pointers at the end of the meaningful elements in both arrays (m-1 for nums1 and n-1 for nums2) and another pointer at the end of nums1 (m+n-1) to indicate the current position to insert the next greatest element.Compare elements from nums1 and nums2 from the end, moving the greater element into the current position in nums1 and adjusting pointers accordingly.Ensure that if nums2 still has elements left after nums1 is exhausted, they are copied over to the beginning of nums1.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) == 0:
            return
        pointer1 = nums1[m-1]
        porinter2 = nums2[]n-1]
        porinter3 = nums1[m+n-1] # do sth about it

        for i in range(n-1):
            if nums2[i] >= nums1[i] and nums2[i] <= nums1[i+1]:
                nums1.insert(i+1, nums2[i])
            elif nums2[i] <= nums1[i]:
                nums1.insert(i, nums2[i])
            elif nums2[i] >= nums1[i+m]:
                nums1.insert(i+m, nums2[i])
        nums1 = nums1[:m+n]
        print(nums1)