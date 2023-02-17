from typing import List


periods: List[dict] = [
    {
        "name": "1",        
        "short": "1",       
        "period": "1",      
        "starttime": "8:00",
        "endtime": "8:45"
    },
    {
        "name": "2",
        "short": "2",
        "period": "2",
        "starttime": "8:50",
        "endtime": "9:35"
    },
    {
        "name": "3",
        "short": "3",
        "period": "3",
        "starttime": "9:50",
        "endtime": "10:35"
    },
    {
        "name": "4",
        "short": "4",
        "period": "4",
        "starttime": "10:40",
        "endtime": "11:25"
    },
    {
        "name": "5",
        "short": "5",
        "period": "5",
        "starttime": "11:40",
        "endtime": "12:25"
    },
    {
        "name": "6",
        "short": "6",
        "period": "6",
        "starttime": "12:30",
        "endtime": "13:15"
    },
    {
        "name": "7",
        "short": "7",
        "period": "7",
        "starttime": "13:20",
        "endtime": "14:05"
    },
    {
        "name": "8",
        "short": "8",
        "period": "8",
        "starttime": "14:10",
        "endtime": "14:55"
    }
]


daysdefs: List[dict] = [
    {
        "name": "Понедельник",
        "short": "Пн",
        "days": "10000",
        "typ": "one",
        "val": 0
    },
    {
        "name": "Вторник",
        "short": "Вт",
        "days": "01000",
        "typ": "one",
        "val": 1
    },
    {
        "name": "Среда",
        "short": "Ср",
        "days": "00100",
        "typ": "one",
        "val": 2
    },
    {
        "name": "Четверг",
        "short": "Чт",
        "days": "00010",
        "typ": "one",
        "val": 3
    },
    {
        "name": "Пятница",
        "short": "Пт",
        "days": "00001",
        "typ": "one",
        "val": 4
    },
    {
        "name": "В любой день",
        "short": "X",
        "days": "10000,01000,00100,00010,00001",
        "typ": "any",
        "val": None
    },
    {
        "name": "Каждый день",
        "short": "E",
        "days": "11111",
        "typ": "all",
        "val": None
    }
]


grades: List[dict] = [
    {
        "name": "Параллель 1",
        "short": "Паралл. 1",
        "grade": "1"
    },
    {
        "name": "Параллель 2",
        "short": "Паралл. 2",
        "grade": "2"
    },
    {
        "name": "Параллель 3",
        "short": "Паралл. 3",
        "grade": "3"
    },
    {
        "name": "Параллель 4",
        "short": "Паралл. 4",
        "grade": "4"
    },
    {
        "name": "Параллель 5",
        "short": "Паралл. 5",
        "grade": "5"
    },
    {
        "name": "Параллель 6",
        "short": "Паралл. 6",
        "grade": "6"
    },
    {
        "name": "Параллель 7",
        "short": "Паралл. 7",
        "grade": "7"
    },
    {
        "name": "Параллель 8",
        "short": "Паралл. 8",
        "grade": "8"
    },
    {
        "name": "Параллель 9",
        "short": "Паралл. 9",
        "grade": "9"
    },
    {
        "name": "Параллель 10",
        "short": "Паралл. 10",
        "grade": "10"
    },
    {
        "name": "Параллель 11",
        "short": "Паралл. 11",
        "grade": "11"
    }
]
