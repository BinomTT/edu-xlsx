from argparse import ArgumentParser, Namespace
from pathlib import Path

from edu_xlsx import XLSXParser


arguments_parser: ArgumentParser = ArgumentParser()
arguments_parser.add_argument("input")
arguments_parser.add_argument("output")
arguments_parser.add_argument("--indent", default=None, type=int, required=False)

arguments: Namespace = arguments_parser.parse_args()
arguments.input = Path(arguments.input)


print(
    "Parsing from {xlsx_filepath}...".format(
        xlsx_filepath = arguments.input.resolve()
    )
)

xlsx_parser: XLSXParser = XLSXParser(
    xlsx_filepath = arguments.input,
    timetable_number = arguments.input.name.split(".")[0].split("_")[-1]
)

xlsx_parser.parse()

xlsx_parser.save(
    json_filepath = arguments.output,
    json_indent = arguments.indent
)

print(
    "Successfully saved to {json_filepath}!".format(
        json_filepath = Path(arguments.output).resolve()
    )
)
