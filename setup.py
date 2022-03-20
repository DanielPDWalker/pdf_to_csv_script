from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="pdf-to-csv-script",
    version="0.1.0",
    description="Quick script to turn pdfs with tables into csv files ",
    author="DanielPDWalker",
    entry_points="""
        [console_scripts]
        pdf_to_csv=pdf_to_csv.cli.commands.root:pdf_to_csv
    """,
    license="MIT",
    install_requires=required,
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
)