class Solution(object):
    """
    1449 / 1481 test cases passed.

    This solution is not approved but almost works
    """
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        specials = {' ': [], '+': [], '-': [], 'e': [], '.': []}
        numbers = list(string.digits)

        # get rid of leading and trailing spaces
        s = s.strip()
        if len(s) == 0:
            return False

        # check spaces into a number
        if len(s) > 0 and " " in s:
            return False
        # retrive info and checks kind of char
        for i in range(len(s)):
            if s[i] in specials:
                specials[s[i]].append(i)

            elif s[i] not in numbers:
                return False
        print specials

        # check spaces into the number
        if specials[' ']:
            return False

        # check negatives and positives
        if len(specials['-']) > 2:
            return False
        elif len(specials['-']) == 1:
            if specials['-'][0] != 0 and (specials['-'][0] - 1) not in specials['e']:
                return False
        elif len(specials['-']) == 2:
            if specials['-'][0] == 0 and (specials['-'][1] - 1) not in specials['e']:
                return False
        elif len(s) - 1 in specials['-']:
            return False

        if len(specials['+']) > 2:
            return False
        elif len(specials['+']) == 1:
            if specials['+'][0] != 0 and (specials['+'][0] - 1) not in specials['e']:
                return False
            if specials['+'][0] - 1 in specials['e'] and specials['+'][0] == len(s) - 1:
                return False
        elif len(specials['-']) == 2:
            if specials['+'][0] == 0 and (specials['+'][1] - 1) not in specials['e']:
                return False
        elif len(s) - 1 in specials['-']:
            return False

            # check e
        if len(specials['e']) > 1:
            return False
        elif len(specials['e']) == 1:
            if specials['e'][0] == 0 or specials['e'][0] == len(s) - 1:
                return False
            elif specials['e'][0] - 1 in specials['.']:
                return False

        # check dot
        if len(specials['.']) >= 3:
            return False
        if len(specials['.']) == 2 and len(specials['e']) == 0:
            return False
        elif len(specials['.']) == 2:
            if specials['.'][0] > specials['e'][0]:
                return False
            elif specials['.'][1] < specials['e'][0]:
                return False
        elif len(specials['.']) == 1:
            if len(s) == 1:
                return False
            elif specials['.'][0] - 1 in specials['e']:
                return False
            elif specials['.'][0] - 1 in specials['-'] and specials['.'][0] == len(s) - 1:
                return False
            elif specials['.'][0] - 1 in specials['+'] and specials['.'][0] == len(s) - 1:
                return False

        return True