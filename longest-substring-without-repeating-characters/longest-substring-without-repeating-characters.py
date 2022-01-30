class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left_pointer = 0
        result = 0
        
        for right_pointer in range(len(s)):
            while s[right_pointer] in charSet:
                charSet.remove(s[left_pointer])
                left_pointer += 1
            charSet.add(s[right_pointer])
            result = max(result, right_pointer - left_pointer + 1)
            
        return result