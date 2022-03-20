import tabula as tb
import os

from pathlib import Path


def convert_pdf(pdf_file_path):

    pdf_file_path = os.path.abspath(pdf_file_path)

    head, tail = os.path.split(pdf_file_path)

    tail = tail.split(".")[0]

    head = Path(head)

    output_path = os.path.join(head, tail + ".csv")

    tb.convert_into(pdf_file_path, output_path, output_format="csv", pages='all')