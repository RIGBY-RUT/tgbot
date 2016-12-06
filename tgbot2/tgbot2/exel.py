import xlrd
import xlwt
import time
import const



while True:

    i = 14;
    j = 2;
    a = 1;
    workbook = xlrd.open_workbook(const.name_exel)
    worksheet = workbook.sheet_by_name(const.name_groop)

    des = int(input('''-----------------------------
Выберите день недели:
      1. Понедельник
      2. Вторник
      3. Среда
      4. Четверг
      5. Пятница
      6. Суббота
      7. Сегодня
      8. Завтра
      '''))

    weeknum = "%U"
    week = int(time.strftime(weeknum))
    if (week % 2 == 0):
        i += 1

    if des == 7:
        daynum = "%w"
        day = int(time.strftime(daynum))
        des = day


    elif des == 8:
        daynum = "%w"
        day = int(time.strftime(daynum))
        des = day + 1
        if (day == 0):
            week += 1

    if des == 1:
        while (a <= 6):
            clock = worksheet.cell(i, j).value
            name = worksheet.cell(i, j + 2).value
            aud = worksheet.cell(i, j + 3).value
            print(a, " пара:", clock, name, aud)
            a += 1
            i += 2


    elif des == 2:
        while (a <= 6):
            clock = worksheet.cell(i + 12, j).value
            name = worksheet.cell(i + 12, j + 2).value
            aud = worksheet.cell(i + 12, j + 3).value
            print(a, " пара:", clock, name, aud)
            a += 1
            i += 2


    elif des == 3:
        while (a <= 6):
            clock = worksheet.cell(i + 24, j).value
            name = worksheet.cell(i + 24, j + 2).value
            aud = worksheet.cell(i + 24, j + 3).value
            print(a, " пара:", clock, name, aud)
            a += 1
            i += 2


    elif des == 4:
        while (a <= 6):
            clock = worksheet.cell(i + 36, j).value
            name = worksheet.cell(i + 36, j + 2).value
            aud = worksheet.cell(i + 36, j + 3).value
            print(a, " пара:", clock, name, aud)
            a += 1
            i += 2


    elif des == 5:
        while (a <= 6):
            clock = worksheet.cell(i + 48, j).value
            name = worksheet.cell(i + 48, j + 2).value
            aud = worksheet.cell(i + 48, j + 3).value
            print(a, " пара:", clock, name, aud)
            a += 1
            i += 2


    elif des == 6:
        while (a <= 6):
            clock = worksheet.cell(i + 60, j).value
            name = worksheet.cell(i + 60, j + 2).value
            aud = worksheet.cell(i + 60, j + 3).value
            print(a, " пара:", clock, name, aud)
            a += 1
            i += 2

