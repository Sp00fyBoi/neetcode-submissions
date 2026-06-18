class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        if len(s) == len(t) :
            for i in s:
                if i in map:
                    map[i] = map[i] + 1
                else:
                    map[i] = 1
            for i in t:
                if i in map:
                    if map[i] == 1:
                        del map[i]
                    else:
                        map[i] = map[i] - 1
            return len(map) == 0
        return False