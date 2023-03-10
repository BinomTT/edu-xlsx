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
    }
]


daysdefs: List[dict] = [
    {
        "name": "Пятница",
        "short": "Пт",
        "days": "00001",
        "typ": "one",
        "val": 0
    },
    {
        "name": "Понедельник",
        "short": "Пн",
        "days": "10000",
        "typ": "one",
        "val": 1
    },
    {
        "name": "Вторник",
        "short": "Вт",
        "days": "01000",
        "typ": "one",
        "val": 2
    },
    {
        "name": "Среда",
        "short": "Ср",
        "days": "00100",
        "typ": "one",
        "val": 3
    }
]


grades: List[dict] = [
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
