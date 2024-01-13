"""
Author: Alex R. Mead
Date: Jan. 2024

Main entry point for pdf2booklet.

"""

from pypdf import PdfReader, PdfWriter

from utils import parse_arguments, blank_page


def main(read_filename, write_filename):
    # Reader and Writer classes
    reader = PdfReader(read_filename)
    writer = PdfWriter()

    # Extract specific pages
    cover_page = reader.pages[0]
    back_page = reader.pages[-1]
    contents = [page for page in reader.pages[1:-1]]

    # Build out PDF page list with blanks
    extra_blanks_needed = 4 - (len(contents) % 4)
    contents += [blank_page for _ in range(0, extra_blanks_needed)]

    # Extract the pages in "print order"
    blocks = int(len(contents) / 4)
    ptr_left, ptr_right = 0, -1
    print_order_list = []
    for _ in range(0, blocks):
        print_order_list = [
            contents[ptr_left+1],
            contents[ptr_right-1],
            contents[ptr_right],
            contents[ptr_left],
        ] + print_order_list
        ptr_left += 2
        ptr_right -= 2

    # Add front and back cover
    print_order_list = print_order_list + [
        blank_page,
        blank_page,
        back_page,
        cover_page,
    ]

    # Add pdf pages to writer
    _ = [writer.add_page(page) for page in print_order_list]

    # Save PDF to file. Print on both sides, landscape, and flip on short edge. 
    # This will create the center fold booklet.
    with open(write_filename, 'wb') as fp:
        writer.write(fp)


if __name__ == "__main__":
    args = parse_arguments()
    main(args.pdf_read_filename, args.pdf_write_filename)