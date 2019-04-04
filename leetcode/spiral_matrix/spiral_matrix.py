class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        row = 0
        column = 0
        max_row = len(matrix) - 1
        max_column = len(matrix[0]) - 1
        min_row = 0
        min_column = 0

        items = len(matrix) * len(matrix[0])
        output = []

        while len(output) != items:
            while column <= max_column:
                output.append(matriz[row][column])
                column += 1

            max_column -= 1

== == == == == == == == == == == == =

while row <= max_row:
    output.append(matrix[row][column])
    row += 1

row -= 1

while column >= min_column:
    output.append(matrix[row][column])
    column -= 1

while row < min_row:
    output.append(matrix[row][column])
    row += 1

for number in matrix[origin + iter:dest - iter]:
    output.append(number)

while index <

    for number in range

    for number in matrix
