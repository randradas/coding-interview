class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """

        result = []
        # Init
        mark = [False] * len(s)

        # Set true
        for word in dict:
            fromsubs = 0
            while fromsubs < len(s):
                subs = s.find(word, fromsubs)
                if subs >= 0:
                    for c in range(subs, subs + len(word)):
                        mark[c] = True
                fromsubs += 1

        # Bold those that are True
        previous = False
        for i in range(len(mark)):
            if mark[i] and not previous:
                result.append('<b>')
                previous = True
            elif not mark[i] and previous:
                result.append('</b>')
                previous = False

            result.append(s[i])

        if mark[len(mark) - 1]:
            result.append('</b>')

        return ''.join(result)
