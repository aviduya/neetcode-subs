class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        s_seen = {}
        t_seen = {}

        for i in range(len(s)): 
            if s[i] in s_seen: 
                s_seen[s[i]] += 1
            else: 
                s_seen[s[i]] = 1
            
            if t[i] in t_seen: 
                t_seen[t[i]] += 1
            else: 
                t_seen[t[i]] = 1
        return s_seen == t_seen