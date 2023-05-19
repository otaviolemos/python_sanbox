class Solution:
    def longestPalindrome(self, s: str) -> str:
        window = len(s)
        for i in range(window, 1, -1):
            start = 0
            end = start + i-1
            while end <= len(s)-1:
                currentString = s[start:end+1]
                if isPalindrome(s[start:end+1]):
                    return currentString
                start += 1
                end = start + i-1
        return s[0]
                    

def isPalindrome(s: str) -> bool:
    if s == s[::-1]:
        return True
    return False