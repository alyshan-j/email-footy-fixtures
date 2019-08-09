# email-footy-fixtures
Scripts for finding soccer games of interest and emailing

## Usage
`run.sh` - I run this script as a cron job to get an email of my matches of interest every morning
`dryrun.sh` - Same as above but without sending an email

## DeSCRIPTions
`read_skysports_fixtures_page.py` was used to crawl a skysports page and create a json dump of a league schedule.
The [skysports site](https://www.skysports.com/premier-league-fixtures).

`fixture_finder.py` prints out matches of interest (based on hardcoded "teams of interest")

`email_sender.py` reads from stdin and emails the content using gmail's smtp server. Some caveats:
1. You must be using a gmail account to send the mail
2. The following environment variables must be set
  - GMAIL_USER
  - GMAIL_PASS
  - RECIEVER

Written & tested with Python 3.6

Enjoy.
