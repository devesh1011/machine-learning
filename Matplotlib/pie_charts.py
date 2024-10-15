import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

# Load the data
df = pd.read_csv("data.csv")

# Extract the necessary columns
lang_responses = df["LanguagesWorkedWith"]

# Initialize a Counter to count language occurrences
language_counter = Counter()

# Update the counter with each response
for response in lang_responses:
    language_counter.update(response.split(";"))

# Prepare the languages and their popularity for the top 15 languages
languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# Plotting the data using a pie chart
plt.figure(figsize=(10, 8))
plt.pie(
    popularity,
    labels=languages,
    autopct="%1.1f%%",
    startangle=140,
    colors=plt.cm.Paired(range(len(languages))),
    wedgeprops={"edgecolor": "black"},
    shadow=True
)
plt.title("Most Popular Programming Languages")
plt.axis("equal")  # Equal aspect ratio ensures the pie is drawn as a circle.

plt.show()
