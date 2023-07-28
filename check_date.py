from sys import argv


def _leap_year(num: int) -> bool:
    flag = False
    if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
        flag = True
    return flag

def check(user_date: str) -> bool:
    flag = False
    day, month, year = map(int, user_date.split('.'))
    if 0 < year < 10000:
        if month in (1, 3, 5, 7, 8, 10, 12) and 0 < day <= 31:
            flag = True
        elif month == 2:
            if _leap_year(year) and 0 < day <= 29:
                flag = True
            elif 0 < day <= 28:
                flag = True
        elif 0 < day <= 30:
            flag = True
    return flag


if __name__ == '__main__':
    print(check(argv[1]))
