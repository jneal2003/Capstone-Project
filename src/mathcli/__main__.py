"""Start a calculator session with python -m mathcli."""

from mathcli.matrix import MatrixError
from mathcli.session import Session

helptext = """\
Commands:
    help matrix
    help session

help matrix
    Show the matrix commands and their syntax.

help session
    Show the session commands and their syntax.
"""

helpmatrix = """\
Commands: 

matrix
    Syntax: matrix NAME
    Create a matrix with this name.
    On each following line, type one row. Separate numbers with spaces.
    Every row must contain the same number of numbers.
    Press Enter on an empty line to store it.
    Example:
        matrix A
        1 2
        3 4
        Press Enter once more, with nothing typed on that line.

vector
    Syntax: vector NAME n1 n2 n3
    Store the numbers after the name as one column.
    Example: vector b 1 2 3

show
    Syntax: show NAME
    Print the matrix saved under that name.
    Example: show A

Operations: 

add
    Syntax: add A B C
    Store A + B under the name C. A and B stay as they were.

sub
    Syntax: sub A B C
    Store A - B under the name C. A and B stay as they were.

mul
    Syntax: mul A B C
    Store A * B under the name C. A and B stay as they were. 
"""

helpsession = """\
Commands: 

list
    Syntax: list
    Print every saved name and its size.
    A saved 2 by 2 matrix named A prints as A 2x2.

delete
    Syntax: delete NAME
    Remove the matrix or vector saved under that name.
    Example: delete A

quit
    Syntax: quit
    Leave the session.
"""


def main():
    session = Session()
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            print()
            return
        if line == "":
            continue
        if line == "quit":
            return
        if line == "help":
            print(helptext, end="")
            continue
        if line == "help matrix":
            print(helpmatrix, end="")
            continue
        if line == "help session":
            print(helpsession, end="")
            continue
        parts = line.split()
        command, args = parts[0], parts[1:]
        if line == "list":
            print(session.list_saved())
            continue
        try:
            if command == "show" and len(args) == 1:
                print(session.show(args[0]))
            elif command == "delete" and len(args) == 1:
                session.delete(args[0])
            elif command == "vector" and len(args) >= 2:
                if _allow_save(session, args[0]):
                    session.vector(args[0], args[1:])
            elif command == "matrix" and len(args) == 1:
                if _allow_save(session, args[0]):
                    _enter(session, args[0])
            elif command == "add" and len(args) == 3:
                if _allow_save(session, args[2]):
                    session.add(args[0], args[1], args[2])
            elif command == "sub" and len(args) == 3:
                if _allow_save(session, args[2]):
                    session.sub(args[0], args[1], args[2])
            elif command == "mul" and len(args) == 3:
                if _allow_save(session, args[2]):
                    session.mul(args[0], args[1], args[2])
            else:
                print("error: unknown command or syntax")
        except MatrixError as exc:
            print(f"error: {exc}")


# Handles the input of the matrix, safeguards against overwriting matricies
def _allow_save(session, name):
    if name not in session.matrices:
        return True
    answer = (
        input(
            f"Matrix {name} already exists, do you want to override? enter yes to override, or no to not\n"
        )
        .strip()
        .lower()
    )
    return answer == "y" or answer == "yes"


def _enter(session, name):
    rows = []
    while True:
        row = input().strip()
        if row == "":
            break
        rows.append(row.split())
    session.enter(name, rows)


if __name__ == "__main__":
    main()
