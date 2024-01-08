Author: Alex R. Mead <br>
Date: Jan. 2024 <br>

Description: Take a PDF and transform it into the proper ordering for printing as a "booklet". <br><br>


# Installation

This is a python module built using Python Version 3.10.8. 

To begin, create a virtual environment and install the dependencies using pip.

```bash
$python -m venv .venv
$source .venv/bin/activate
$python -m pip install -U pip
$python -m pip install -r requirements.txt
```

# Running the Application
```bash
$python main.py --pdf_read_filename="<input_pdf_filename>" --pdf_write_filename="<output_pdf_filename>"
```


