class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): 
            return False 
        
        s_amt = {}
        t_amt = {}

        # By this time we can assume that the amount of chars in both strings are the same
        for i in range(len(s)): 
            if s[i] in s_amt: 
                s_amt[s[i]] += 1 
            else:
                s_amt[s[i]] = 1
            
            if t[i] in t_amt: 
                t_amt[t[i]] += 1
            else: 
                t_amt[t[i]] = 1
        
        return s_amt == t_amt
