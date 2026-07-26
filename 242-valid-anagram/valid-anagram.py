class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen={}
        frequency={}

        for ch in s:
            if ch in seen:

                seen[ch]+=1
            else:

                seen[ch]=1

        for cj in t:
            if cj in frequency:

                frequency[cj]+=1
            else:

                frequency[cj]=1

        return seen==frequency
            