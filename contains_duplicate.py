def hasDuplicate(self, nums: List[int]) -> bool:
  seen = set()
  for num in nums: 
    if num in seen: 
      return True 
    else: 
      seen.add(num)
  return False

# This function checks if a list contains any duplicates using a set
# A set is used because it allows for constant time lookups and avoids duplicates 
# Time Complexity: O(n): Iterating through the list once 
# Space Complexity: O(n): In worst case, all n elements are stored in the set