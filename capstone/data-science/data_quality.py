import os
import pandas as pd

# read the fake data
df = pd.read_csv("capstone/data-science/data/incidents.csv")

# turn the date text into real dates so we can find the first and last
df["created_at"] = pd.to_datetime(df["created_at"])

closed = df[df["status"] == "closed"]

# each line of the quality file: a name and a number or value
checks = [
    ["total_rows", len(df)],
    ["closed_rows", len(closed)],
    ["open_rows", len(df) - len(closed)],
    ["first_date", df["created_at"].min()],
    ["last_date", df["created_at"].max()],
    ["days_covered", (df["created_at"].max() - df["created_at"].min()).days],
    ["blank_category", df["category"].isna().sum()],
    ["blank_title", df["title"].isna().sum()],
    ["closed_rows_missing_resolution_time", closed["resolution_hours"].isna().sum()],
]

os.makedirs("capstone/data-science/output", exist_ok=True)
result = pd.DataFrame(checks, columns=["check", "value"])
result.to_csv("capstone/data-science/output/data_quality.csv", index=False)
print(result)
