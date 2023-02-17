from pathlib import Path
from setuptools import setup, find_packages
from re import findall as re_findall, M as ReM

import sys


WORK_DIR = Path(__file__).parent

PACKAGE_NAME = "edu_xlsx"
MINIMAL_PY_VERSION = (3, 7)

if sys.version_info < MINIMAL_PY_VERSION:
    raise RuntimeError(
        "{package_name} works only with Python {minimal_py_version}+".format(
            package_name = PACKAGE_NAME,
            minimal_py_version = ".".join(map(str, MINIMAL_PY_VERSION))
        )
    )


init_py_string = (WORK_DIR / PACKAGE_NAME / "__init__.py").read_text("utf-8")


setup(
    name = PACKAGE_NAME,
    version = re_findall(r"^__version__ = \"([^']+)\"$", init_py_string, ReM)[0],
    description = "Excel file parser to Edupage's response format",
    license = "MIT",
    author = "Aryn Yklas",
    author_email = "arynyklas@gmail.com",
    packages = find_packages(),
    python_requires = ">=3.7",
    install_requires = (WORK_DIR / "requirements.txt").read_text("utf-8").strip().split("\n"),
    include_package_data = False
)
