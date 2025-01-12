class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.split()
        print(s_list)
        s_list=list(reversed(s_list))
        return " ".join(s_list)
        