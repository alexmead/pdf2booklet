"""
Author: Alex R. Mead
Date: January 2024

Description:
Utils functions and resources to help build out PDF booklets.
"""
import argparse

from pypdf import PdfReader

reader = PdfReader('boiler_plate/blank_page.pdf')
blank_page = reader.pages[0]

def parse_arguments():
    """Returns command line arguments to the calling script."""
    parser = argparse.ArgumentParser(description="Reorders a PDF document for printing as a booklet.")
    parser.add_argument('--pdf_read_filename', required=True)
    parser.add_argument('--pdf_write_filename', required=True)
    # TODO: Add in "create cover" with "title" flag
    return parser.parse_args()
