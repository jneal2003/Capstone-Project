"""Matrices are stored as NumPy arrays."""

from fractions import Fraction

import numpy as np


class MatrixError(ValueError):
    """A matrix could not be built or used."""


def parse_number(token):
    try:
        return Fraction(token)
    except ValueError as exc:
        raise MatrixError(f"not a number: {token}") from exc


class Matrix:
    def __init__(self, rows):
        if not rows or any(len(row) == 0 for row in rows):
            raise MatrixError("a matrix needs at least one entry")
        width = len(rows[0])
        if any(len(row) != width for row in rows):
            raise MatrixError("every row must have the same number of entries")
        self.data = np.array(rows, dtype=object)

    @property
    def rows(self):
        return int(self.data.shape[0])

    @property
    def cols(self):
        return int(self.data.shape[1])

    def size(self):
        return f"{self.rows}x{self.cols}"

    def __str__(self):
        return "\n".join(" ".join(str(value) for value in row) for row in self.data)


# Matrix Operations


def add_matricies(m1, m2) -> Matrix:
    if m1.rows != m2.rows or m1.cols != m2.cols:
        raise MatrixError("only matricies of the same size can be added")
    rows = []
    for i in range(m1.rows):
        row = []
        for j in range(m1.cols):
            row.append(m1.data[i, j] + m2.data[i, j])
        rows.append(row)
    return Matrix(rows)


def sub_matricies(m1, m2) -> Matrix:
    if m1.rows != m2.rows or m1.cols != m2.cols:
        raise MatrixError("only matricies of the same size can be subtracted")
    rows = []
    for i in range(m1.rows):
        row = []
        for j in range(m1.cols):
            row.append(m1.data[i, j] - m2.data[i, j])
        rows.append(row)
    return Matrix(rows)


def multiply_matrices(m1, m2) -> Matrix:
    if m1.cols != m2.rows:
        raise MatrixError("invalid dimensions for matrix multiplication.")

    # NumPy's @ operator performs matrix multiplication
    result_data = m1.data @ m2.data

    return Matrix(result_data.tolist())
