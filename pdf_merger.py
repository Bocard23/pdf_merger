#!/usr/bin/env python

import os
from PyPDF2 import PdfFileReader, PdfFileMerger

path = os.getcwd()
pdfs = [pdf for pdf in os.listdir(path) if pdf.endswith("pdf")]
pdf_merger = PdfFileMerger()

if len(pdfs) > 0:
    for file in pdfs:
        pdf_merger.append(PdfFileReader(os.path.join(path, file), "rb"))

    pdf_merger.write(os.path.join(path, "merged.pdf"))
else:
    print("no pdfs found at: %s" % path)

