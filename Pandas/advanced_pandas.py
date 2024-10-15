import pandas as pd

people = {
    "first": ["Devesh", "Ankit", "Prince"],
    "last": ["K", "K", "K"],
    "email": ["deveshk237@gmail.com", "deveshk237@gmail.com", "deveshk237@gmail.com"],
}

df = pd.read_csv(
    "stack-overflow-developer-survey-2023/survey_results_public.csv",
    index_col="ResponseId",
)
# print(df.loc[0:3, "EdLevel":"YearsCode"])
df.sort_index()
print(df.head())

people_df = pd.DataFrame(people)

people_df.set_index(
    "email", inplace=True
)  # sets the index of table to a specific column

# print(people_df)
# print(df.index)

# using indexes on out dataset
