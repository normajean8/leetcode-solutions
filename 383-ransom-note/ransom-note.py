class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen={}
        freq={}

        for ch in ransomNote:
            if ch in seen:
                seen[ch]+=1
            else:
                seen[ch]=1

        for cj in magazine:
            if cj in freq:
                freq[cj]+=1

            else:
                freq[cj]=1

        for ch in seen:
            if ch not in freq:
                return False

            if seen[ch] > freq[ch]:

                return False

        return True 