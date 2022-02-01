

def first_day(year) -> int:
    bis = year + year//4 - year//100 + year//400
    return bis % 7

def dia_n(hoy, n):
    return (hoy + n) % 7

dicc_dia = {
    0: "Domingo",
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado"
}

if __name__ == "__main__":
    print(first_day(2022))