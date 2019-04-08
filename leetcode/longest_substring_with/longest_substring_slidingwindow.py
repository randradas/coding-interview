class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if len(s) == 0 or k == 0: return 0

        left = 0
        right = 0
        maxlen = 0
        items = {}

        while right <= len(s) - 1:
            if s[right] not in items.keys():
                items[s[right]] = 1
            elif s[right] in items.keys():
                items[s[right]] += 1

            while len(items.keys()) > k:
                if items[s[left]] == 1:
                    items.pop(s[left])
                else:
                    items[s[left]] -= 1

                left += 1

            maxlen = max(maxlen, right - left + 1)
            right += 1

        return maxlen
