
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        pivot = 0
        subs = ""
        subs_aux = ""
        distinct_aux = []

        while pivot <= (len(s) - 1):
            for c in s[pivot:]:
                subs_aux += c
                if c not in distinct_aux:
                    distinct_aux.append(c)

                if len(distinct_aux) > k:
                    break

                if len(subs_aux) > len(subs):
                    subs = subs_aux

            subs_aux = ""
            distinct_aux = []
            pivot += 1

        return len(subs)