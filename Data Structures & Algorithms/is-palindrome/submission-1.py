class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter_str = "".join([char for char in s if char.isalnum()]).lower()
        return filter_str == filter_str[::-1]