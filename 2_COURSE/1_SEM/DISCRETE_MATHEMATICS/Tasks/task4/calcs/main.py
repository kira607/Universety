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
        print(f"$ \\beta_{i} = {bb} $\\\\")
        i += 1
