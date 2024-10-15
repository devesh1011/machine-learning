import pandas as pd
from matplotlib import pyplot as plt

# Read the CSV file
file_path = "all_currencies.csv"  # Adjust this path if necessary
df = pd.read_csv(file_path)

# Convert the 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d %I-%p")

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df["Date"], df["Close"], alpha=0.5)

# Add titles and labels
plt.title("Scatter Plot of ETHUSD Close Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Close Price")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
