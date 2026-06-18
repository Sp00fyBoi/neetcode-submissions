class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        copy = strs[:]

        for i , val in enumerate(strs):
            strs[i] = "".join(sorted(val))

        map = {}

        for i , val in enumerate(strs):
            if val in map:
                map[val].append(copy[i])
            else:
                map[val] = [copy[i]]
        
        result = []
        for key in map:
            result.append(map[key])
        
        return result