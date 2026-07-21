class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)
        for i in range(len(s)//2):
            temp = s[length-i-1]
            s[length-i-1] = s[i]
            s[i] = temp

        """
        Do not return anything, modify s in-place instead.
        """
        