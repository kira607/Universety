from datetime import date, timedelta

if __name__ == '__main__':
    b = [
        "b_1b_2",
        "b_1b_2b_2",
        "b_2b_1b_1",
        "b_3b_2b_1b_1",
        "b_2b_1b_2b_3b_2b_1",
        "b_1b_1b_2b_3b_2b_1", ]

    i = 1
    for bb in b:
        # print(f"$ \\beta_{i} = {bb} $\\\\")
        i += 1

    print("1 \oplus 0 \oplus 1 \oplus 1 \oplus 1 \oplus 1 = ".replace("\oplus", "^"), end="")
    print(1 ^ 0 ^ 1 ^ 1 ^ 1 ^ 1)

    print("1 \oplus 1 \oplus 1 \oplus 1 \oplus 1 \oplus 1 = ".replace("\oplus", "^"), end="")
    print(1 ^ 1 ^ 1 ^ 1 ^ 1 ^ 1)

    print("0 \oplus 1 \oplus 1 \oplus 1 \oplus 1 \oplus 1 = ".replace("\oplus", "^"), end="")
    print(0 ^ 1 ^ 1 ^ 1 ^ 1 ^ 1)

    print("1 \oplus 1 \oplus 1 \oplus 1 \oplus 1 \oplus 1 = ".replace("\oplus", "^"), end="")
    print(1 ^ 1 ^ 1 ^ 1 ^ 1 ^ 1)

    print(0^0^1^0)


