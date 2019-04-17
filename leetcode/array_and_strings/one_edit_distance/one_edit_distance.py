class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        diff = 0
        length_diff = abs(len(s) - len(t))

        if s == t: return False
        if length_diff > 1: return False

        if length_diff == 0:
            i = 0
            while diff <= 1 and i < len(s):
                if s[i] == t[i]:
                    i += 1
                else:
                    i += 1
                    diff += 1
        else:
            si = 0
            ti = 0
            while diff <= 1 and si < len(s) and ti < len(t):
                if s[si] == t[ti]:
                    si += 1
                    ti += 1
                elif len(s) > len(t):
                    si += 1
                    diff += 1
                elif len(s) < len(t):
                    ti += 1
                    diff += 1

        if diff > 1:
            return False
        else:
            return True
