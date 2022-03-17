# Date conversor
# Convert American style dates to European style (MM-DD-YYYY to DD-MM-YYYY)
# dateconversor.py <path to files>

import re, os, sys, shutil

us_style = r'([0|1]?\d)-([0-3]?\d)-(\d{4})'
us_dateRegex = re.compile(us_style)

dates_path = "."
if len(sys.argv) > 1:
    dates_path = (sys.argv[1])

files = os.listdir(dates_path)

for f in files:
    date = us_dateRegex.search(f)
    if date:
        newName = re.sub(us_style, '%s-%s-%s', f)
        newName = newName % (date.group(2),date.group(1),date.group(3))
        shutil.move(dates_path + "\\" + f,dates_path + "\\" + newName)
