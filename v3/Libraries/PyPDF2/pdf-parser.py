# Examples from https://automatetheboringstuff.com/chapter13/


"""
#    >>> import PyPDF2
#    >>> pdfFileObj = open('meetingminutes.pdf', 'rb')
#    >>> pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# ❶ >>> pdfReader.numPages
#    19
# ❷ >>> pageObj = pdfReader.getPage(0)
# ❸ >>> pageObj.extractText()
#    'OOFFFFIICCIIAALL BBOOAARRDD MMIINNUUTTEESS Meeting of March 7, 2015
#    \n     The Board of Elementary and Secondary Education shall provide leadership
#    and create policies for education that expand opportunities for children,
#    empower families and communities, and advance Louisiana in an increasingly
#    competitive global market. BOARD of ELEMENTARY and SECONDARY EDUCATION '
"""

import PyPDF2
