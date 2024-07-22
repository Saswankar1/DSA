class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to map Roman numerals to their integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        # Iterate over the Roman numeral string from left to right
        for char in s:
            current_value = roman_to_int[char]
            # If the current value is greater than the previous value, it means we encountered a subtractive combination
            if current_value > prev_value:
                # Subtract twice the previous value (since it was added once before)
                total += current_value - 2 * prev_value
            else:
                total += current_value
            prev_value = current_value
        
        return total
