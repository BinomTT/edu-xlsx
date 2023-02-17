from pydantic import BaseModel

from .utils import generate_hex_color

from typing import List, Optional, Any


T_TIMEOFF = List[List[List[str]]]

TIMEOFF: List[List[List[str]]] = [
    [
        [
            "1"
        ]
    ]
]


class Class(BaseModel):
    id: str
    name: str
    short: str
    teacherid: Optional[str] = ""
    classroomids: Optional[List[str]] = []
    bell: Optional[str] = "0"
    color: Optional[str] = generate_hex_color()
    timeoff: Optional[T_TIMEOFF] = TIMEOFF
    printsubjectpictures: Optional[bool] = True
    classroomid: Optional[str] = None


class Subject(BaseModel):
    id: str
    name: str
    short: str
    color: Optional[str] = generate_hex_color()
    picture_url: Optional[str] = ""
    timeoff: Optional[T_TIMEOFF] = TIMEOFF
    contract_weight: Optional[int] = 1


class Classroom(BaseModel):
    id: str
    name: str
    short: str
    buildingid: Optional[str] = ""
    sharedroom: Optional[bool] = False
    needssupervision: Optional[bool] = False
    color: Optional[str] = generate_hex_color()
    nearbyclassroomids: Optional[List[Any]] = []


class Teacher(BaseModel):
    id: str
    firstname: str
    lastname: str
    short: str
    nameprefix: Optional[str] = ""
    namesuffix: Optional[str] = ""
    gender: Optional[str] = ""
    bell: Optional[str] = ""
    color: Optional[str] = generate_hex_color()
    fontcolorprint: Optional[str] = ""
    fontcolorprint2: Optional[str] = ""
    fontcolorscreen: Optional[str] = ""
    timeoff: Optional[T_TIMEOFF] = TIMEOFF


class Group(BaseModel):
    id: str
    name: str
    classid: str
    entireclass: bool
    ascttdivision: str
    divisionid: str
    okgroup: Optional[bool] = False
    students_count: Optional[Any] = None
    color: Optional[str] = generate_hex_color()


class Lesson(BaseModel):
    id: str
    subjectid: str
    teacherids: List[str]
    groupids: List[str]
    classids: List[str]
    classroomidss: List[List[str]]
    termsdefid: str
    weeksdefid: str
    daysdefid: str
    count: Optional[int] = 1
    durationperiods: Optional[int] = 1
    terms: Optional[str] = "1"
    seminargroup: Optional[Any] = None
    bell: Optional[str] = ""
    studentids: Optional[List[Any]] = []
    groupnames: Optional[List[str]] = [""]


class Card(BaseModel):
    id: str
    lessonid: str
    period: str
    days: str
    weeks: str
    classroomids: List[str]
