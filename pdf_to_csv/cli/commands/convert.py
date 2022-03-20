"""CLI 'convert' command"""

import click


from pdf_to_csv.cli.commands.root import pdf_to_csv
from pdf_to_csv.pdf_converter import convert_pdf


@pdf_to_csv.command(
    "convert", short_help="Convert a pdf to csv"
)
@click.argument("path", type=click.Path(exists=True))
def convert(path):
    """Convert a pdf from path into a csv in output dir"""

    convert_pdf(path)
