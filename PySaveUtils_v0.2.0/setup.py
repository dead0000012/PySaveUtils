from pathlib import Path

from setuptools import find_packages, setup

BASE_DIR = Path(__file__).parent

about: dict = {}
exec((BASE_DIR / "pysaveutils" / "__about__.py").read_text(encoding="utf-8"), about)

setup(
    name="PySaveUtils",
    version=about["__version__"],
    author="Dead0000012",
    author_email="dead0000012@gmail.com",
    description="Набор утилит для генерации случайных данных и проверки пользовательского ввода.",
    long_description=BASE_DIR.joinpath("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/dead0000012/PySaveUtils",  # если есть GitHub
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
