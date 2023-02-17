from typing import List


periods: List[dict] = [
    {
        "period": "0",
        "name": "0",
        "short": "0",
        "starttime": "13:20",
        "endtime": "14:05"
    },
    {
        "period": "1",
        "name": "1",
        "short": "1",
        "starttime": "14:10",
        "endtime": "14:55"
    },
    {
        "period": "2",
        "name": "2",
        "short": "2",
        "starttime": "15:00",
        "endtime": "15:45"
    },
    {
        "period": "3",
        "name": "3",
        "short": "3",
        "starttime": "16:00",
        "endtime": "16:45"
    },
    {
        "period": "4",
        "name": "4",
        "short": "4",
        "starttime": "16:50",
        "endtime": "17:35"
    },
    {
        "period": "5",
        "name": "5",
        "short": "5",
        "starttime": "17:50",
        "endtime": "18:35"
    },
    {
        "period": "6",
        "name": "6",
        "short": "6",
        "starttime": "18:40",
        "endtime": "19:25"
    },
    {
        "period": "7",
        "name": "7",
        "short": "7",
        "starttime": "19:30",
        "endtime": "20:15"
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
    }
]
