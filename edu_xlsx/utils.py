from re import Pattern as RePattern, compile as regex_compile
from itertools import chain as itertools_chain
from random import randint

from typing import List, Dict, Tuple, Any, Optional


digit_6_re: RePattern = regex_compile(r"^\d{6}$")
digit_3_dot_3_re: RePattern = regex_compile(r"^\d{3}\.\d{3}$")
letters_re: RePattern = regex_compile(r"^[A-Z]+")


def table_to_dict_id_obj(table: List[object]) -> Dict[str, object]:
    return {
        item_data.id: item_data
        for item_data in table
    }


def pretty_time(seconds: int) -> str:
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    return "{hours}:{minutes:02d}".format(
        hours = hours,
        minutes = minutes
    )


def build_ids(items: List[dict]) -> List[dict]:
    results: List[dict] = []

    for i, item in enumerate((
        list(itertools_chain(*[
            item
            for item in items
        ]))
        if items and isinstance(items[0], list)
        else
        items
    ), 1):
        data = dict(
            id = "*" + str(i)
        )
        data.update(item)
        results.append(data)

    return results


def build_periods(lessons_count: int, lesson_time: int, lessons_start_time: int, breaks: List[int]) -> List[dict]:
    results: List[dict] = []

    prev_value: int = 0

    lesson_time *= 60
    lessons_start_time *= 60

    for lesson_num, break_value in zip(range(1, lessons_count + 1), breaks):
        starttime: int = (
            prev_value
            if prev_value
            else
            lessons_start_time
        )

        endtime: int = starttime + lesson_time

        data: dict = dict(
            name = str(lesson_num),
            short = str(lesson_num),
            period = str(lesson_num),
            starttime = pretty_time(starttime),
            endtime = pretty_time(endtime)
        )

        results.append(data)

        prev_value = endtime + break_value * 60

    results = build_ids(
        items = results
    )

    return results


def build_groups(classids: List[str]) -> List[Tuple[dict, dict, dict]]:
    results: List[Tuple[dict, dict, dict]] = []

    for classid in classids:
        results.append(dict(
            name = "Весь класс",
            classid = classid,
            entireclass = True,
            divisiontag = "0"
        ))

        results.append(dict(
            name = "1 группа",
            classid = classid,
            entireclass = False,
            divisiontag = "1"
        ))

        results.append(dict(
            name = "2 группа",
            classid = classid,
            entireclass = False,
            divisiontag = "1"
        ))

    return results


def generate_hex_color() -> str:
    return ("#%06x" % randint(0, 0xFFFFFF)).upper()


def get_short_first_chars(string: str) -> str:
    return "".join([
        word[0]
        for word in string.split(" ")
        if word
    ])


def chunker(collection: List[Any], count: int) -> List[List[Any]]:
    return [
        collection[i:i + count]
        for i in range(0, len(collection), count)
    ]


def parse_classroom_names(classroom_names_str: str, classrooms_from_name: Optional[Dict[str, Any]]=None) -> List[str]: # TODO: replace `Any` with `models.Class`
    if digit_6_re.match(
        string = classroom_names_str
    ):
        classroom_names_str = classroom_names_str[:3] + "," + classroom_names_str[-3:]

    elif digit_3_dot_3_re.match(
        string = classroom_names_str
    ):
        classroom_names_str = classroom_names_str.replace(".", ",", 1)

    classroom_names: List[str] = []

    for classroom_name in classroom_names_str.split(","):
        classroom_name = classroom_name.strip()

        if not classroom_name or (classrooms_from_name and classroom_name in classrooms_from_name):
            continue

        # TODO
        if classroom_name.lower()[-1] in ["a", "а"]:
            classroom_name = classroom_name[:-1]
        # if classroom_name[-2].isdigit() and classroom_name.lower()[-1] in ["a", "а"]:
        #     classroom_name = classroom_name[:-1] + "-а"
        # else:
        if not ("С" in classroom_name and "Б" in classroom_name):
            classroom_name = classroom_name.split(" ", 1)[0]

        classroom_names.append(classroom_name)

    return classroom_names


def parse_coordinate_ord(coordinate: str) -> int:
    coordinate_letters: str = letters_re.match(
        string = coordinate
    ).group(0)

    return ord((
        "Z"
        if coordinate_letters[0] == "A" and len(coordinate_letters) > 1
        else
        coordinate_letters[0]
    )) + sum([
        ord(letter) - 64
        for letter in coordinate_letters[1:]
    ])
