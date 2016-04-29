#coding=utf8

import numpy as np
from docx import Document
from docx.document import Document as Doc
from docx.table import  Table
from docx.text.paragraph import Paragraph

def linalg():
    a = np.array([[5,-1,2], [-2,6,9], [-7,5,-3]])
    print a
    b = np.array([7,0,-7])
    print b
    x = np.linalg.solve(a,b)
    print x
    print np.dot(a,x)

def readdocx():
    d = Document('20160509.docx')
    for tab in d.tables:
        row_count = len(tab.rows)
        col_count = len(tab.columns)
        for row in tab.rows:
            for cell in row.cells:
                print(cell.text)
    for sec in d.sections:
        print sec.start_type

if __name__ == "__main__":
    pass
