class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # it can only be anagram if the strings have the same len
        if len(s) != len(t): 
            return False

        # We can use a hash map to store seen chars and initialize a count as the value refering to the amount weve seen the char. 
        s_freq = {}
        t_freq = {}

        #len(s) == len(t) we can create a loop of len(s) times: 
        for i in range(len(s)):
            # Check to see if the given char is in both maps else init the value a the map
            if s[i] in s_freq: 
                s_freq[s[i]] += 1
            else: 
                s_freq[s[i]] = 1

            if t[i] in t_freq: 
                t_freq[t[i]] += 1
            else:
                t_freq[t[i]] = 1

        # Return the result of if the maps match each other. 
        return s_freq == t_freq

                