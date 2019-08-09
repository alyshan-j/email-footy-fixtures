import sys
import re
import json

"""
Crawler to read fixtures from https://www.skysports.com/premier-league-fixtures
Usage: python3 read_skysports_fixtures_page.py <input> <output>
<input> html page dump of the skysports fixtures page 
<output> output file for the json dump of the fixtures
"""
if len(sys.argv) < 3:
    print("Please provide output file name")
    exit()

out_file = sys.argv[2]

lines = []
with open(sys.argv[1]) as file_:
    lines = file_.readlines()

fixtures = {}
month, day = "", ""
for line in lines:
    #looking for the line below, and extracting the date
    #<h4 class="fixres__header2">Sunday 30th September</h4>
    if "fixres__header2" in line:
        date = line[line.index(">")+1 : line.index("<",line.index(">"))]
        month, day = date.split(" ")[2], re.sub("\D", "", date.split(" ")[1])
    #looking for the line below, and extracting the matchup
    #https://www.skysports.com/football/west-ham-vs-man-utd/3908
    elif "-vs-" in line:
        if month not in fixtures:
            fixtures[month] = {day : []}
        if day not in fixtures[month]:
            fixtures[month][day] = []

        fixtures[month][day].append(line.split('/')[4])

with open(out_file, "w") as output:
    output.write(json.dumps(fixtures, indent=2))
