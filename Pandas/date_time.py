import pandas as pd
from datetime import datetime
import matplotlib as mp

# Read the CSV file
df = pd.read_csv("all_currencies.csv")

# Convert the 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d %I-%p")

# print(df.heald(10))

# Get the day name
# print(df.loc[0, "Date"].day_name())

df["Day Name"] = df["Date"].dt.day_name()

# print(df.head(10))

# getting the minimum date
# print(df["Date"].min())
# getting the maximum date
df["Date"].max()

df.set_index("Date", inplace=True)

df.sort_index(inplace=True)

# Now you can slice the data using date strings
mean_close = df["2020-01":"2020-02"]["Close"].mean()
# print(mean_close)

# getting the max of the currency on that specific day
# print(df['2020-01-01']['High'].max())

highs = df["High"].resample("D").max()

# resampling of dataframe
print(
    df.resample("W").agg(
        {"Close": "mean", "High": "max", "Low": "min", "Volume": "sum"}
    )
)
