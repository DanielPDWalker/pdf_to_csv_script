import tabula as tb

tb.convert_into("input/data.pdf", "output/data.csv", output_format="csv", pages='all')