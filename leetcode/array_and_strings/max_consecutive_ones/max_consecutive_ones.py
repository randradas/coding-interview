class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxconsec = 0
        current = 0

        for n in nums:
            if n == 1:
                current += 1
            elif n == 0:
                maxconsec = max(maxconsec, current)
                current = n

        maxconsec = max(maxconsec, current)

        return maxconsec