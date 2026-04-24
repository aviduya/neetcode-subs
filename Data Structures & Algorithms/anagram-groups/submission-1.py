class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_bank = {} 

        for word in strs: 
            word_key = "".join(sorted(word))

            if word_key in word_bank: 
                word_bank[word_key].append(word)
            else: 
                word_bank[word_key] = [word]
        
        return list(word_bank.values())