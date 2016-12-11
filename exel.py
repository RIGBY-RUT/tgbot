# -*- coding: utf-8 -*-

import xlrd
import xlwt
import time
import const

"""
1. Понедельник
2. Вторник
3. Среда
4. Четверг
5. Пятница
6. Суббота
7. Сегодня
8. Завтра
"""
def getTimeTable(group_name, exel_name, decision):
    workbook = xlrd.open_workbook(exel_name)
    try:
        worksheet = workbook.sheet_by_name(group_name)
    except xlrd.biffh.XLRDError:
        print ("Ошибка имени группы")
        return ("Неправильное название группы, может быть, этой группы нет в новой таблице.\n", 0)
    dataLine = 14;
    dataColumn = 1;

    if worksheet.cell(0, 0).value == xlrd.empty_cell.value:
        dataColumn += 1

    weeknum = "%U"
    week = int(time.strftime(weeknum))
    if (week % 2 == 0):
        dataLine += 1

    if decision == 7:
        daynum = "%w"
        day = int(time.strftime(daynum))
        decision = day
    elif decision == 8:
        daynum = "%w"
        day = int(time.strftime(daynum))
        decision = day + 1
        if (day == 0):
            week += 1

    ans = ""
    if 1 <= decision and decision <= 6:
        a = 1
        while (a <= 6):
            weekdayShift = 12 * (decision - 1)
            clock = worksheet.cell(dataLine + weekdayShift, dataColumn).value
            name = worksheet.cell(dataLine + weekdayShift, dataColumn + 2).value
            aud = worksheet.cell(dataLine + weekdayShift, dataColumn + 3).value
            ans += str(a) + u" пара:" \
                + clock + ' ' + \
                name + ' ' + aud + u"\n"
            a += 1
            dataLine += 2
    else:
        ans = "ошибка, возможно, индекс неправильный день недели: {})".format(decision)
    return (ans, 1)
