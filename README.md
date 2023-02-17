# Excel file parser to Edupage's response format


This library parses .XLSX files to Edupage's response format
Library's main idea - integrate output .JSON files to use in [BinomTTBot](https://github.com/arynyklas/BinomTTBot)


### Python modules and libraries used: (not built-in)
- [prettytable](pypi.org/project/prettytable) - 3.6.0
- [openpyxl](pypi.org/project/openpyxl) - 3.1.0
- [pydantic](pypi.org/project/pydantic) - 1.10.4


### Setup
Install this library with command:
`python -m pip install -U git+https://github.com/arynyklas/edu-xlsx.git`


### Use examples
To use as CLI application:
`python -m edu_xlsx timetable_examples/input_timetable.xlsx timetable_examples/output_timetable.json`

To use as iibrary:
```python
from edu_xlsx import XLSXParser

xlsx_parser: XLSXParser = XLSXParser(
    xlsx_filepath = "timetable_examples/input_timetable.xlsx",
    timetable_number = "1"
)

xlsx_parser.parse()

xlsx_parser.save(
    json_filepath = "timetable_examples/output_timetable.json",
    json_indent = None # Optional integer argument
)
```


#### Files
File examples:
- .XLSX - [timetable_examples/input_timetable.xlsx](timetable_examples/input_timetable.xlsx)
- .JSON - [timetable_examples/output_timetable.json](timetable_examples/output_timetable.json)


### License
[MIT](LICENSE)
