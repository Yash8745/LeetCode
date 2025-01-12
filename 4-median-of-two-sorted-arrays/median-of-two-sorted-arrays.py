# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         res=0
#         merge_array=[]
#         def merge():
#             i=0
#             j=0
#             while i<len(nums1) and j<len(nums2):
#                 if i>j:
#                     merge_array.append(nums1[i])
#                     i+=1
#                 elif j>i:
#                     merge_array.append(nums2[j])
#                     j+=1
#                 else:
#                     merge_array.append(nums1[i])
#                     merge_array.append(nums2[j])
#                     i+=1
#                     j+=1
#             while i<len(nums1):
#                 merge_array.append(nums1[i])
#                 i+=1
#             while j<len(nums2):
#                 merge_array.append(nums2[j])
#                 i+=1
#         merge()
#         n = len(merge_array)
#         median=0
#         mid = n // 2  

#         if n % 2 == 0:  
#             median= (merge_array[mid - 1] + merge_array[mid]) / 2
#         else:  
#             median= merge_array[mid]
#         return median
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            # Handle edges
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            # Check for valid partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # Found correct partition
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                # Move partitionX to the left
                high = partitionX - 1
            else:
                # Move partitionX to the right
                low = partitionX + 1

        raise ValueError("Input arrays are not sorted")





