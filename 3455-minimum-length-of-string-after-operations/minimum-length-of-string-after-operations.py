class Solution:
    def minimumLength(self, s: str) -> int:

        freq=Counter(s)
        res=0
        for i in freq.keys():
            if freq[i]%2:
                res+=1
            else:
                res+=2
        return res