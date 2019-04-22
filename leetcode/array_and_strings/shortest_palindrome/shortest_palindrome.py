class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        mirror = ""
        output = ""
        i = len(s) - 1

        # mirror my input
        mirror = s[::-1]

        # find a substring
        j = len(mirror) - 1
        i = 0
        while j >= 0:
            subs = mirror[i:].find(s[:j])
            if subs > 0:
                output = s[j:]
                j = -1
            elif subs == 0 and j == len(s) - 1:
                j = -1
            elif subs == 0 and j == 0:
                output = s[j + 1:]
                j = -1
            else:
                j -= 1
                i += 1

        if len(output) == len(s):
            return output[::-1][:-1] + s

        return output[::-1] + s