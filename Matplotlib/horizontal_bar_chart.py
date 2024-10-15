import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

plt.xkcd()

df = pd.read_csv("data.csv")

ids = df["Responder_id"]
lang_responses = df["LanguagesWorkedWith"]

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(";"))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

# use this method we can change the vertical to horizontal
plt.barh(languages, popularity)

plt.title("Most Popular Languages")

plt.xlabel("Number of People who use")

plt.tight_layout()

plt.show()
