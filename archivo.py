

def first_day(year: int) -> int:
    year-=1
    bis = year+1 + year//4 - year//100 + year//400
    return bis % 7

def dia_n(hoy, n):
    return (hoy + n) % 7

def es_bis(year):
    return (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0)

dicc_dia = {
    0: "Domingo",
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado"
}

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def which_day_is(day, month, year):
    first = first_day(year)

    num_of_days = 0
    for i in range(month-1):
        num_of_days += dias_mes[i]
    
    if es_bis(year) and month > 2:
        num_of_days+=1
    
    #print(num_of_days)
    num_of_days += day - 1
    
    #print(first)
    
    day_int = (first + num_of_days) % 7
    return dicc_dia[day_int]


if __name__ == "__main__":
    # print(first_day(2016))
    print(which_day_is(1, 1, 2015))