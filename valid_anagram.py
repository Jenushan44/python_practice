class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        
        for letter_s in s: 
            if letter_s not in s_dict: 
                s_dict[letter_s] = 1
            else: 
                s_dict[letter_s] += 1 

        for letter_t in t: 
            if letter_t not in s_dict: 
                return False 
            else: 
                if s_dict[letter_t] < 0: 
                    return False
                else: 
                    s_dict[letter_t] -= 1
        
        for count in s_dict.values(): 
            if count != 0: 
                return False

        return True

# This function checks if two strings are anagrams by using a dictionary to count character frequencies
# A dictionary is used because it allows for constant time lookups and updates for each character
# Time Compexity: O(n) because I iterate through both strings once to build and update the dictionary 
# Space Complexity: O(1) because the dictionary stores at most 26 characters (a-z) which is constant space