# Sample systems

These are the hand solutions for the tests. A vector is written as a one-column matrix.

## System 1: normal

Every pivot is nonzero. No row swap.

Augmented matrix:

    [ 1  1  1  |  6 ]
    [ 2  1  1  |  7 ]
    [ 1  1  2  |  9 ]

Row operations:

1. R2 = R2 - 2 R1

        [ 1  1  1  |  6 ]
        [ 0 -1 -1  | -5 ]
        [ 1  1  2  |  9 ]

2. R3 = R3 - R1

        [ 1  1  1  |  6 ]
        [ 0 -1 -1  | -5 ]
        [ 0  0  1  |  3 ]

3. R2 = -1 R2

        [ 1  1  1  |  6 ]
        [ 0  1  1  |  5 ]
        [ 0  0  1  |  3 ]

4. R1 = R1 - R2

        [ 1  0  0  |  1 ]
        [ 0  1  1  |  5 ]
        [ 0  0  1  |  3 ]

5. R2 = R2 - R3

        [ 1  0  0  |  1 ]
        [ 0  1  0  |  2 ]
        [ 0  0  1  |  3 ]

Reduced row echelon form:

    [ 1  0  0  |  1 ]
    [ 0  1  0  |  2 ]
    [ 0  0  1  |  3 ]

Determinant of the coefficient matrix: -1

Solution: x = 1, y = 2, z = 3

## System 2: row swap

The first pivot is zero, so the first move is a swap.

Augmented matrix:

    [ 0  1  1  |  5 ]
    [ 1  1  1  |  6 ]
    [ 1  2  1  |  8 ]

Row operations:

1. Swap R1 and R2

        [ 1  1  1  |  6 ]
        [ 0  1  1  |  5 ]
        [ 1  2  1  |  8 ]

2. R3 = R3 - R1

        [ 1  1  1  |  6 ]
        [ 0  1  1  |  5 ]
        [ 0  1  0  |  2 ]

3. R3 = R3 - R2

        [ 1  1  1  |  6 ]
        [ 0  1  1  |  5 ]
        [ 0  0 -1  | -3 ]

4. R3 = -1 R3

        [ 1  1  1  |  6 ]
        [ 0  1  1  |  5 ]
        [ 0  0  1  |  3 ]

5. R2 = R2 - R3

        [ 1  1  1  |  6 ]
        [ 0  1  0  |  2 ]
        [ 0  0  1  |  3 ]

6. R1 = R1 - R2 - R3

        [ 1  0  0  |  1 ]
        [ 0  1  0  |  2 ]
        [ 0  0  1  |  3 ]

Reduced row echelon form:

    [ 1  0  0  |  1 ]
    [ 0  1  0  |  2 ]
    [ 0  0  1  |  3 ]

Determinant of the coefficient matrix: 1

Solution: x = 1, y = 2, z = 3

## System 3: no solution

Augmented matrix:

    [ 1  1  1  |  1 ]
    [ 2  2  2  |  3 ]
    [ 1  2  3  |  4 ]

Row operations:

1. R2 = R2 - 2 R1

        [ 1  1  1  |  1 ]
        [ 0  0  0  |  1 ]
        [ 1  2  3  |  4 ]

2. R3 = R3 - R1

        [ 1  1  1  |  1 ]
        [ 0  0  0  |  1 ]
        [ 0  1  2  |  3 ]

3. Swap R2 and R3

        [ 1  1  1  |  1 ]
        [ 0  1  2  |  3 ]
        [ 0  0  0  |  1 ]

4. R1 = R1 - R2

        [ 1  0 -1  | -2 ]
        [ 0  1  2  |  3 ]
        [ 0  0  0  |  1 ]

Reduced row echelon form:

    [ 1  0 -1  | -2 ]
    [ 0  1  2  |  3 ]
    [ 0  0  0  |  1 ]

Determinant of the coefficient matrix: 0

Solution: no solution. The last row says 0 = 1.

## Arithmetic

A =

    [ 1  2 ]
    [ 3  4 ]

B =

    [ 5  6 ]
    [ 7  8 ]

A + B =

    [  6   8 ]
    [ 10  12 ]

A - B =

    [ -4  -4 ]
    [ -4  -4 ]

A * B =

    [ 19  22 ]
    [ 43  50 ]

2 * A =

    [ 2  4 ]
    [ 6  8 ]

Transpose of A =

    [ 1  3 ]
    [ 2  4 ]

Dot product of u = [1, 2, 3] and v = [4, 5, 6]: 32

Matrix times vector:

    [ 1  2 ]   [ 1 ]   [  5 ]
    [ 3  4 ] * [ 2 ] = [ 11 ]

Size mismatch for addition: A is 2 by 2, and this matrix is 2 by 3.

    [ 1  0  2 ]
    [ 0  1  3 ]

Size mismatch for the dot product: [1, 2] and [4, 5, 6].