"""
usefull functions
"""

def test_int(x):
    return all(isinstance(ele, int) for ele in x)


def test_float(x):
    return all(isinstance(ele, float) for ele in x)


def test_row(mtrx):
    n = len(mtrx[0])
    for row in mtrx:
        if len(row) != n:
            return False
    return True

def add_matrices(A, B):
    # Check if the dimensions of A and B are the same
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions.")
    return [
        [A[i][j] + B[i][j] for j in range(len(A[0]))]
        for i in range(len(A))
    ]


def subtract_matrices(A, B):
    # Check if the dimensions of A and B are the same
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions.")
    return [
        [A[i][j] - B[i][j] for j in range(len(A[0]))]
        for i in range(len(A))
    ]


def multiply_matrices(m_a, m_b):
    """
        doc
        """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(x, list) for x in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(x, list) for x in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == []:
        raise ValueError("m_a can't be empty")
    if all(len(x) for x in m_a) == 0:
        raise ValueError("m_a can't be empty")
    if m_b == []:
        raise ValueError("m_b can't be empty")
    if all(len(x) for x in m_b) == 0:
        raise ValueError("m_b can't be empty")
    if not all(test_int(x) for x in m_a) \
            and not all(test_float(x) for x in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(test_int(x) for x in m_b) \
            and not all(test_float(x) for x in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if not test_row(m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not test_row(m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    r1 = []
    i1 = 0

    for a in m_a:
        r2 = []
        i2 = 0
        num = 0
        while (i2 < len(m_b[0])):
            num += a[i1] * m_b[i1][i2]
            if i1 == len(m_b) - 1:
                i1 = 0
                i2 += 1
                r2.append(num)
                num = 0
            else:
                i1 += 1
        r1.append(r2)

    return r1



def read_matrix_from_file(file):
    with open(file, 'r') as file:
        lines = file.readlines()

    # Extract number of rows and columns from the first two lines
    rows = int(lines[0].split('=')[1])
    cols = int(lines[1].split('=')[1])

    # Initialize the matrix with zeros
    matrix = [[0 for _ in range(cols)]] * rows
    print(f"rows = {len(matrix)}")
    print(f"cols = {len(matrix[0])}")

    # Populate the matrix with the values from the file
    for line in lines[2:]:
        line = line.strip("(")
        line = line.strip("\n")
        line = line.strip(")")
        row, col, value = list(map(int, line.split(", ")))
        matrix[row][col-1] = value
    return matrix

