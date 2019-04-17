class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        water_units = 0
        water_level = 0

        while left < right:
            if height[right] >= height[left]:
                if height[left] >= water_level:
                    water_level = height[left]
                else:
                    water_units += water_level - height[left]

                left += 1
            else:
                if height[right] >= water_level:
                    water_level = height[right]
                else:
                    water_units += water_level - height[right]

                right -= 1

        return water_units