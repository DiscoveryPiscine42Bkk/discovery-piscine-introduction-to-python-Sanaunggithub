# main.py
from checkmate import checkmate

def main():

    # success board
    board = """\
R...
.K..
..P.
...."""

#     board = """\
# ..
# .K\
# """
    checkmate(board)

if __name__ == "__main__":
    main()
