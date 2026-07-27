class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq={}

        for cj in magazine:
            if cj in freq:
                freq[cj]+=1

            else:
                freq[cj]=1

        for ch in ransomNote:
            if ch not in freq:
                return False

            if freq[ch]==0:
                return False
            else:
                freq[ch]-=1

        return True 