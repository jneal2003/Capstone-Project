import pytest

from mathcli.matrix import MatrixError
from mathcli.session import Session


# addition and subtraction
def test_add_matrices_working():
    session = Session()
    session.enter("A", [["1", "2"], ["3", "4"]])
    session.enter("B", [["5", "6"], ["7", "8"]])
    session.add("A", "B", "C")
    assert session.list_saved() == "A 2x2\nB 2x2\nC 2x2"
    assert session.show("C") == "6 8\n10 12"
    assert session.show("A") == "1 2\n3 4"
    assert session.show("B") == "5 6\n7 8"


def test_sub_matrices_working():
    session = Session()
    session.enter("A", [["1", "2"], ["3", "4"]])
    session.enter("B", [["5", "6"], ["7", "8"]])
    session.sub("A", "B", "D")
    assert session.list_saved() == "A 2x2\nB 2x2\nD 2x2"
    assert session.show("D") == "-4 -4\n-4 -4"
    assert session.show("A") == "1 2\n3 4"
    assert session.show("B") == "5 6\n7 8"


def test_add_size_mismatch():
    session = Session()
    session.enter("A", [["1", "2"], ["3", "4"]])
    session.enter("B", [["1", "0", "2"], ["0", "1", "3"]])
    with pytest.raises(MatrixError):
        session.add("A", "B", "C")
    assert session.list_saved() == "A 2x2\nB 2x3"
    assert session.show("A") == "1 2\n3 4"


def test_sub_size_mismatch():
    session = Session()
    session.enter("A", [["1", "2"], ["3", "4"]])
    session.enter("B", [["1", "0", "2"], ["0", "1", "3"]])
    with pytest.raises(MatrixError):
        session.sub("A", "B", "D")
    assert session.list_saved() == "A 2x2\nB 2x3"
    assert session.show("A") == "1 2\n3 4"


def test_mul_matrices_working():
    session = Session()
    session.enter("A", [["1", "2"], ["3", "4"]])
    session.enter("B", [["5", "6"], ["7", "8"]])
    session.mul("A", "B", "C")
    assert session.list_saved() == "A 2x2\nB 2x2\nC 2x2"
    assert session.show("C") == "19 22\n43 50"
    assert session.show("A") == "1 2\n3 4"
    assert session.show("B") == "5 6\n7 8"


def test_mul_matrix_times_vector():
    session = Session()
    session.enter("A", [["1", "2"], ["3", "4"]])
    session.vector("B", ["1", "2"])
    session.mul("A", "B", "C")
    assert session.show("C") == "5\n11"
    assert session.show("A") == "1 2\n3 4"


def test_mul_size_mismatch():
    session = Session()
    session.enter("A", [["1", "2"], ["3", "4"]])
    session.enter("B", [["1", "0", "2"], ["0", "1", "3"]])
    with pytest.raises(MatrixError):
        session.mul("B", "A", "C")
    assert session.list_saved() == "A 2x2\nB 2x3"
    assert session.show("A") == "1 2\n3 4"
