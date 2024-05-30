##################
##  Vit Pavlik  ##
##   xpavli0a   ##
##    251301    ##
##     2024     ##
##################

#
# sudoku to propositional logic
#

def get_index(x: int, y: int, value: int) -> int:
    """
    returns an index of the variable at position x, y (0 to 8)
    with value (1 to 9)

    example values:
    ```
    x=0, y=0, value=1 -> 0
    x=0, y=0, value=2 -> 1
    x=0, y=0, value=3 -> 2
    x=1, y=0, value=1 -> 9
    x=1, y=0, value=2 -> 10
    x=2, y=0, value=1 -> 18
    x=2, y=0, value=2 -> 19
    x=0, y=1, value=1 -> 81
    x=0, y=1, value=2 -> 82

    ```
    """
    assert 0 <= x <= 8
    assert 0 <= y <= 8
    assert 1 <= value <= 9

    return 9 * 9 * y + 9 * x + value - 1


def main() -> None:
    i = 0
    for y in range(9):
        for x in range(9):
            for value in range(1, 10):
                print(f"{x=}, {y=}, {value=} -> {get_index(x, y, value)}")
                i += 1
                if i > 82:
                    print("abort")
                    exit()


if __name__ == "__main__":
    main()
