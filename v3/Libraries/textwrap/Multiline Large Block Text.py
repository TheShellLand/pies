import textwrap

# ...

def getCalendarHeader(self):
    print
    textwrap.dedent("""\
            BEGIN:VCALENDAR
            PRODID:-//Atlassian Software Systems//Confluence Calendar Plugin//EN
            VERSION:2.0
            CALSCALE:GREGORIAN
            X-WR-CALNAME;VALUE=TEXT:
            X-WR-CALDESC;VALUE=TEXT:
            """)
