class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        seen={}
        freq={}

        for i in range(len(t)):
            ch=s[i]
            cj=t[i]

            if ch in seen:
                if seen[ch]!=cj:
                    return False

            else:
                 seen[ch]=cj

            if cj in freq:
                if freq[cj]!=ch:
                    return False

            else:
                freq[cj]=ch

        return True


        