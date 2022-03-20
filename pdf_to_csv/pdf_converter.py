import tabula as tb
import os


def convert_pdf(pdf_file_path):

    os.path.abspath(pdf_file_path)

    head, tail = os.path.split(pdf_file_path)

    tail = tail.split(".")[0]

    tb.convert_into(pdf_file_path, f"{head}/{tail}.csv", output_format="csv", pages='all')