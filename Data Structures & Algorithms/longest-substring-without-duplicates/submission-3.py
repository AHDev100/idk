class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l, r = 0, 0
        ret = 0
        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                r += 1
                ret = max(ret, r - l)
            else:
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
        return ret