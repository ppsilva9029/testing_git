

def first_day(year) -> int:
    bis = year + year//4 - year//100 + year//400
    return bis % 7

if __name__ == "__main__":
    print(first_day(2022))