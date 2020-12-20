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

    date_format = "%d.%m.%Y"
    my_date = date(2020, 9, 14)

    def switch(days):
        if days == 3:
            return 4
        if days == 4:
            return 3

    days = 4

    while my_date < date(2021, 1, 1):
        print(my_date.strftime(date_format))
        my_date += timedelta(days=days)
        days = switch(days)
