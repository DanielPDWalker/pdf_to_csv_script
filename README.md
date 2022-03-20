# PDF with tables to CSV

## Installing and Using this script

First make sure you have python3 on your system. If not go to (python.org)[https://www.python.org/] and install it. 

Make sure you add it to your path!

### Create a new python virtual environment.

`python -m venv venv`

### Activate your new python virtual environment.

Windows CMD:
`venv\Scripts\activate`

Linux/Mac
`source venv/bin/activate`

### Pip install this git repository

`pip install git+https://github.com/DanielPDWalker/pdf_to_csv_script.git`

### In your terminal type

`pdf_to_csv convert <relative_path_to_your_pdf>`

Once the script has run there should be a csv file with the same name as you pdf in the directory that your pdf is in.
