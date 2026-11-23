# DATA.md

## Where the data comes from
All fake data (synthetic). A Python script makes it with a fixed random seed.
No real names or customer info. Saved as a CSV file, not in the database.

## What each row has
id, created_at, category, title, status, resolved_at, resolution_hours

## Rules I planted
- 10,000+ rows over about 120 days
- 5 categories: Scanners, Dispatch app, Printers, Logins, Network
- Weekdays only, 8am to 5pm, with busier mornings (9 and 10am)
- Volume grows a little each week
- Most incidents close in a few hours, and a few take days
- Logins are fastest, Network is slowest
- Newest incidents are more likely still open

## Limits
- I put the patterns in myself, so results show the method, not real Harborlight facts.
- Resolution time is how long an incident stays open, not how long an agent works on it.
