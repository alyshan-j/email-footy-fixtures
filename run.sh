#!/bin/bash

cd "$(dirname "$0")"

curl https://www.skysports.com/serie-a-fixtures > out.txt
python3 read_skysports_fixtures_page.py out.txt seriea-matches.json

curl https://www.skysports.com/premier-league-fixtures > out.txt
python3 read_skysports_fixtures_page.py out.txt pl-matches.json

source set_email_vars
python3 fixture_finder.py | python3 email_sender.py
