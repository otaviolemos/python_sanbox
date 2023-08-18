class Solution:
    def longestPalindrome(self, s: str) -> str:
        strlen = len(s)
        for window in range(strlen, 1, -1):
            start = 0
            end = start + window-1
            while end <= len(s)-1:
                currentString = s[start:end+1]
                if isPalindrome(s[start:end+1]):
                    return currentString
                start += 1
                end = start + window-1
        return s[0]
                    

def isPalindrome(s: str) -> bool:
    if s == s[::-1]:
        return True
    return False