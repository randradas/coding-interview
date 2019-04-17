class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        alphanums = [chr(x) for x in range(ord('a'), ord('z') + 1)]
        for n in range(10):
            alphanums.append(str(n))
        s_lower = s.lower()

        l_i = 0
        r_i = len(s_lower) - 1

        palindrome = True

        while l_i < r_i and palindrome:
            l_chr = str(s_lower[l_i])
            r_chr = str(s_lower[r_i])

            if l_chr in alphanums and r_chr in alphanums:
                if l_chr != r_chr:
                    palindrome = False
                else:
                    l_i += 1
                    r_i -= 1

            if l_chr not in alphanums:
                l_i += 1

            if r_chr not in alphanums:
                r_i -= 1

        return palindrome
