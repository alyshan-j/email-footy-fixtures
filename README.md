# email-footy-fixtures
Scripts for finding soccer games of interest and emailing

`read_skysports_fixtures_page.py` was used to crawl a skysports page and create a json dump of a league schedule.
The [skysports site](https://www.skysports.com/premier-league-fixtures).

I have included the json dump of the English Premier league (`pl_matches.json`) and the Italian Serie A league (`seriea_matches.json`) 2017/2018 schedules.

`fixture_finder.py` is hardcoded to only read these files, but should be simple to extend ...

`email_sender.py` reads from stdin and emails the content using gmail's smtp server. Some caveats:
1. You must be using a gmail account to send the mail
2. The following environment variables must be set
  - GMAIL_USER
  - GMAIL_PASS
  - RECIEVER


Written & tested with Python 3.6

Enjoy.
