class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        seen={}
        freq={}
        words=s.split()

        if len(pattern) != len(words):
            return False

        for i in range (len(words)):
            ch=pattern[i]
            cj=words[i]

            if ch in seen:
                if seen[ch] != cj:
                    return False

            else:
                seen[ch]=cj

            if cj in freq:
                if freq[cj] !=ch:
                    return False

            else:
                freq[cj] = ch
        return True

        