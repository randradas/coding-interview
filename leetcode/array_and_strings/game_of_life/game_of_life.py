class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        output = []
        memory = {}
        neighs_num = 0
        rows = len(board)
        if rows > 0:
            columns = len(board[0])

            for x in range(rows):
                for y in range(columns):
                    neighs_num = 0
                    for w in range(x - 1, x + 2):
                        if w >= 0 and w < rows:
                            for z in range(y - 1, y + 2):
                                if z >= 0 and z < columns and (x, y) != (w, z):
                                    print("\t%s,%s" % (w, z))
                                    if (w, z) in memory.keys():
                                        neigh_value = memory[(w, z)]
                                    else:
                                        neigh_value = board[w][z]

                                    if neigh_value > 0:
                                        neighs_num += 1

                    not_action = False

                    if neighs_num < 2:
                        new_value = 0
                    elif neighs_num > 3:
                        new_value = 0
                    elif neighs_num == 3:
                        new_value = 1
                    else:
                        not_action = True

                    if not not_action:
                        memory[(x, y)] = board[x][y]
                        board[x][y] = new_value