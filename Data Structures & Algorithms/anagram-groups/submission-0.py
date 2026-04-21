class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_keys = {}
        
        for word in strs: 
            sorted_key = ''.join(sorted(word))

            if sorted_key in word_keys: 
                word_keys[sorted_key].append(word)
            else: 
                word_keys[sorted_key] = [word]
        
            
        return list(word_keys.values())

