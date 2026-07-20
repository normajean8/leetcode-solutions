class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        best = 0

        for right in range (len(s)):
            current_char = s[right]

            if current_char in seen and seen[current_char] >= left:
                left = seen[current_char] + 1

            seen[current_char]=right

            best=max(best, right - left + 1)
        
        return best