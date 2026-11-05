import pytest

from mathcli.matrix import MatrixError
from mathcli.session import Session


def test_enter_list_show_delete_is_working():
    session = Session()
    session.enter("A", [["1", "2"], ["3", "4"]])
    assert session.list_saved() == "A 2x2"
    assert session.show("A") == "1 2\n3 4"
    session.delete("A")
    assert session.list_saved() == "(none)"


def test_vector_is_one_column_matrix():
    session = Session()
    session.vector("b", ["1", "2", "3"])
    assert session.show("b") == "1\n2\n3"
    assert session.list_saved() == "b 3x1"


def test_invalid_matrix_saves_nothing():
    session = Session()
    session.enter("A", [["1", "2"], ["3", "4"]])
    with pytest.raises(MatrixError):
        session.enter("B", [["1", "2"], ["3"]])
    assert list(session.matrices) == ["A"]


def test_unknown_name_leaves_store_unchanged():
    session = Session()
    session.enter("A", [["1"]])
    with pytest.raises(MatrixError):
        session.show("missing")
    with pytest.raises(MatrixError):
        session.delete("missing")
    assert session.show("A") == "1"
