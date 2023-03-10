from argparse import ArgumentParser, Namespace
from pathlib import Path


argument_parser: ArgumentParser = ArgumentParser()
argument_parser.add_argument("input")
argument_parser.add_argument("output")
argument_parser.add_argument("--indent", default=None, type=int, required=False)
argument_parser.add_argument("--use-temp", action="store_true", default=False)

arguments: Namespace = argument_parser.parse_args()
arguments.input = Path(arguments.input)
arguments.output = Path(arguments.output)


if arguments.use_temp:
    from edu_xlsx import TempXLSXParser as XLSXParser
else:
    from edu_xlsx import XLSXParser


print(
    "Parsing from \"{xlsx_filepath}\" ...".format(
        xlsx_filepath = arguments.input.resolve()
    )
)

xlsx_parser: XLSXParser = XLSXParser(
    xlsx_filepath = arguments.input,
    timetable_number = arguments.input.name.split(".")[-2].split("_")[-1]
)

xlsx_parser.parse()

xlsx_parser.save(
    json_filepath = arguments.output,
    json_indent = arguments.indent
)

print(
    "Successfully saved to \"{json_filepath}\"!".format(
        json_filepath = arguments.output.resolve()
    )
)
