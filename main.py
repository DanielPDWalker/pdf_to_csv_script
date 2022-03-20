import tabula as tb

tail = "data"

tb.convert_into("input/data.pdf", f"output/{tail}.csv", output_format="csv", pages='all')