class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []

        row = 0
        column = 0
        max_row = len(matrix) - 1
        max_column = len(matrix[0]) - 1
        min_row = 0
        min_column = 0

        items = len(matrix) * len(matrix[0])
        print(items)
        output = []

        while len(output) != items:
            while column <= max_column and len(output) != items:
                print("x:%s y:%s" % (row, column))
                output.append(matrix[row][column])
                column += 1

            min_row += 1
            row += 1
            column -= 1

            while row <= max_row and len(output) != items:
                print("x:%s y:%s" % (row, column))
                output.append(matrix[row][column])
                row += 1

            max_column -= 1
            row -= 1
            column -= 1

            while column >= min_column and len(output) != items:
                print("x:%s y:%s" % (row, column))
                output.append(matrix[row][column])
                column -= 1

            max_row -= 1
            column += 1
            row -= 1

            while row >= min_row and len(output) != items:
                print("x:%s y:%s" % (row, column))
                output.append(matrix[row][column])
                row -= 1

            min_column += 1
            row += 1
            column += 1
            print(len(output))

        return output
