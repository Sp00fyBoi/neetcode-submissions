class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        from collections import defaultdict

        anagram_map = defaultdict(list)

        for word in strs:
            count = [0] * 26  # for 'a' to 'z'

            for char in word:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)  # lists can't be dict keys
            anagram_map[key].append(word)

        return list(anagram_map.values())
