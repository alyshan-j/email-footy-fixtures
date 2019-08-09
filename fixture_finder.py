import json
from datetime import datetime

pl_matches = {}
seriea_matches = {}
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#teams of interest for each league
pl_toi = ['arsenal', 'man-utd', 'tottenham', 'man-city', 'chelsea', 'liverpool']
seriea_toi = ['juventus', 'napoli', 'lazio', 'inter']

#prints matches of interest given fixtures and teams of interest
def print_moi(match_dict, toi, month, day, INC):
    if month in match_dict:
        for matchday, fixtures in match_dict[month].items():
            if int(matchday) >= day and int(matchday) <= day+INC:
                for fix in fixtures:
                    team1, team2 = fix.split('-vs-')
                    if team1 in toi and team2 in toi:
                        print(month + " " + matchday + " " + fix)

#todo use command line args
with open('pl-matches.json') as data:
    pl_matches = json.load(data)

with open('seriea-matches.json') as data:
    seriea_matches = json.load(data)

month = months[datetime.now().month-1]
day = datetime.now().day
INC = 5
print_moi(seriea_matches, seriea_toi, month, day, INC)
print_moi(pl_matches, pl_toi, month, day, INC)
#todo print_moi should handle month rollover
if day > 26:
    next_month = months[datetime.now().month%12]
    print_moi(pl_matches, pl_toi, next_month, 1, INC)
    print_moi(seriea_matches, seriea_toi, next_month, 1, INC)

