# Rotate image: leetcode 48
def rotate(self, matrix: List[List[int]]) -> None:
    # Time complexity: O(n2)
    # Space complexity: O(1)

    # get the size of the matrix
    l, r = 0, len(matrix[0])-1

    # move from outer edges to inner 
    while l < r:
        # move along each side of the square
        for i in range(r-l):
            top, bottom = l, r

            # get the top left
            tmp = matrix[top][l+i]

            # move bottom left to top left
            matrix[top][l+i] = matrix[bottom-i][l] 
            # move bottom right to bottom left
            matrix[bottom-i][l] = matrix[bottom][r-i]
            # move top right to bottom right
            matrix[bottom][r-i] = matrix[top+i][r]
            # move top left (tmp) to top right
            matrix[top+i][r] = tmp

        # move from outer edges to inner 
        l += 1
        r -= 1
