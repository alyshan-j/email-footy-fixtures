import json
from datetime import datetime

INC = 5

pl_matches = {}
seriea_matches = {}

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#teams of interest for each league
pl_toi = ['arsenal', 'man-utd', 'tottenham', 'man-city', 'chelsea', 'liverpool']
seriea_toi = ['juventus', 'napoli', 'lazio', 'inter']

month = months[datetime.now().month-1]
day = datetime.now().day

#prints matches of interest given fixtures and teams of interest
def print_moi(match_dict, toi):
    if month in match_dict:
        for matchday, fixtures in match_dict[month].items():
            if int(matchday) >= day and int(matchday) <= day+INC:
                for fix in fixtures:
                    team1, team2 = fix.split('-vs-')
                    if team1 in toi and team2 in toi:
                        print(month + " " + matchday + " " + fix)

with open('pl-matches.json') as data:
    pl_matches = json.load(data)

with open('seriea-matches.json') as data:
    seriea_matches = json.load(data)

print_moi(pl_matches, pl_toi)
print_moi(seriea_matches, seriea_toi)

