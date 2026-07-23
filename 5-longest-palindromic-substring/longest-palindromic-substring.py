class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
      
        def expand(left, right):

            while left>=0 and right <len(s) and s[left] == s[right]:
                left -=1
                right+=1

            return s[left+1:right]

        length=""

        for i in range (len(s)):

            odd=expand(i,i)

            length= max(odd, length, key=len)

            even= expand(i,i+1)

            length=max(even,length, key=len)

        return length


        