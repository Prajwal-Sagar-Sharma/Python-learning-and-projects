import re,shutil,os
def find_american_date(text):
    american_date=re.compile(r'''
    ^.*?
    0|1?\d-
    0|1|2|3?\d-
    19|20?\d\d
    .*?$
    ''',re.VERBOSE)
    value=american_date.findall(text)
    return value

print(find_american_date("athisis20-30-40and12-12-1912"))