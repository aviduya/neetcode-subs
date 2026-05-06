class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = {}

        for string in strs:
            sorted_key = "".join(sorted(string))

            if sorted_key in sorted_map: 
                sorted_map[sorted_key].append(string)
            else:
                sorted_map[sorted_key] = [string]
        
        return list(sorted_map.values())