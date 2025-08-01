class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums): 
            comp = target - num 
            if comp in seen: 
                return [seen[comp], i]
            else: 
                seen[num] = i

# This function finds two indices that add up to the target
# A dictionary is used to store seen numbers and their indices for constant-time lookups
# For each number, it checks if the complement (target - num) has already been seen
# If the complement exists, it returns the indices of both numbers
# Time Complexity: O(n): Iterates through the list once with constant-time dictionary operations
# Space Complexity: O(n): In the worst case, it stores all n elements in the dictionary