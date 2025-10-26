from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Mapping of digits to corresponding letters
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        res = []
        
        # Helper function for backtracking
        def backtrack(index: int, current: str):
            # Base case: if current combination length == digits length
            if index == len(digits):
                res.append(current)
                return
            
            # Get the possible letters for the current digit
            for letter in phone_map[digits[index]]:
                backtrack(index + 1, current + letter)
        
        backtrack(0, "")
        return res
