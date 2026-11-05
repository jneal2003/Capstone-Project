"""Saved matrices for one calculator session."""

from mathcli.matrix import (
    Matrix,
    MatrixError,
    add_matricies,
    multiply_matrices,
    parse_number,
    sub_matricies,
)


class Session:
    def __init__(self):
        self.matrices = {}

    def enter(self, name, rows):
        matrix = Matrix([[parse_number(token) for token in row] for row in rows])
        self.matrices[name] = matrix

    def vector(self, name, values):
        self.enter(name, [[value] for value in values])

    def show(self, name):
        if name not in self.matrices:
            raise MatrixError(f"unknown name: {name}")
        return str(self.matrices[name])

    def delete(self, name):
        if name not in self.matrices:
            raise MatrixError(f"unknown name: {name}")
        del self.matrices[name]

    def list_saved(self):
        if not self.matrices:
            return "(none)"
        return "\n".join(
            f"{name} {matrix.size()}" for name, matrix in self.matrices.items()
        )

    def _get(self, name):
        if name not in self.matrices:
            raise MatrixError(f"unknown name: {name}")
        return self.matrices[name]

    # operations
    def add(self, left, right, result):
        total = add_matricies(self._get(left), self._get(right))
        self.matrices[result] = total

    def sub(self, left, right, result):
        difference = sub_matricies(self._get(left), self._get(right))
        self.matrices[result] = difference

    def mul(self, left, right, result):
        product = multiply_matrices(self._get(left), self._get(right))
        self.matrices[result] = product
