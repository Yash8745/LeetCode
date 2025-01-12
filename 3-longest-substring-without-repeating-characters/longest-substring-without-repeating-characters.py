class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        track = set()
        res = 0

        while right < len(s):
            if s[right] not in track:
                track.add(s[right])  # Add the character to the set
                res = max(res, len(track))  # Update the result
                right += 1
            else:
                # Remove the left character to shrink the window
                track.remove(s[left])
                left += 1

        return res
