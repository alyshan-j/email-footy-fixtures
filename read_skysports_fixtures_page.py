#crawler to read fixtures from https://www.skysports.com/premier-league-fixtures
import sys
import re
import json

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

with open("matches.json", "w") as output:
    output.write(json.dumps(fixtures, indent=2))
