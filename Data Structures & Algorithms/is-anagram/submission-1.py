class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        # Count characters in s
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Reduce counts using t
        for ch in t:
            if ch not in freq:
                return False
            freq[ch] -= 1
            if freq[ch] == 0:
                del freq[ch]

        return not freq
