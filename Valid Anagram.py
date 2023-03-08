class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for i in s:
            if i in dict_s:
                dict_s[i] += 1
            else:
                dict_s[i] = 1
        # print(dict_s)
        for j in t:
            if j in dict_s:
                dict_s[j] -= 1
            else:
                return False
        print(dict_s)
        for k in dict_s.values():
            # print(k)
            if k != 0:
                return False
        return True
