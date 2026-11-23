import csv
import os
import random
from datetime import datetime, timedelta

# the seed makes the "random" data come out the same every time I run this
random_seed = 42
random.seed(random_seed)

# first day of fake data, and the pretend "right now"
start_day = datetime(2026, 7, 24)
now = datetime(2026, 11, 20, 17, 0)

# the 5 types of problems, and about how many hours each one takes to fix
# (same order in both lists: Logins = 1 hour, Network = 9 hours)
categories = ["Logins", "Printers", "Scanners", "Dispatch app", "Network"]
average_hours = [1, 2, 4, 6, 9]

# one title for each category, in the same order as above
titles = ["Can't log in", "Label printer jammed", "Handheld won't charge",
          "Dispatch app crashing", "Wifi dropping"]
vague_title = "Not working"   # sometimes people don't say what is wrong

# hours people report problems (9 and 10 are in there more, so mornings are busy)
hours = [8, 9, 9, 9, 10, 10, 10, 11, 12, 13, 14, 15, 16]

# most fixes are quick, but a few take a really long time
# (lots of small numbers, just one 10, so slow ones are rare)
multipliers = [0.5, 0.5, 0.5, 1, 1, 1, 1, 2, 2, 3, 5, 10]

rows = []
day = start_day

# go through every day from the start until "now"
while day <= now:

    # skip Saturday and Sunday (weekday numbers 5 and 6)
    if day.weekday() < 5:

        # which week are we in? week 0, 1, 2...
        week_number = (day - start_day).days // 7

        # a few more incidents each week, so the volume slowly grows
        incidents_today = 120 + week_number * 3

        # make one fake incident for each of today's incidents
        for i in range(incidents_today):
            minute = random.randint(0, 59)
            created = day.replace(hour=random.choice(hours), minute=minute)

            # pick a category (0 to 4) and use that number to look up its info
            pick = random.randint(0, 4)
            category = categories[pick]

            # about 1 in 10 incidents gets the vague title
            if random.random() < 0.10:
                title = vague_title
            else:
                title = titles[pick]

            # fix time = the category's usual time x a random multiplier
            fix_hours = average_hours[pick] * random.choice(multipliers)
            resolved = created + timedelta(hours=fix_hours)

            # if it would finish after "now", it isn't fixed yet, so it's still open
            if resolved > now:
                status = "open"
                resolved = ""
                fix_hours = ""
            else:
                status = "closed"

            rows.append([created, category, title, status, resolved, fix_hours])

    # move on to the next day
    day = day + timedelta(days=1)

# put the oldest incidents first
rows.sort()

# make a data folder (if there isn't one) and save everything in a CSV file
os.makedirs("capstone/data-science/data", exist_ok=True)
file = open("capstone/data-science/data/incidents.csv", "w", newline="")
writer = csv.writer(file)

# first row is the column names
writer.writerow(["id", "created_at", "category", "title", "status", "resolved_at", "resolution_hours"])

# then one row per incident, numbered 1, 2, 3...
number = 1
for row in rows:
    writer.writerow([number] + row)
    number = number + 1
file.close()

print("Wrote", len(rows), "rows")
