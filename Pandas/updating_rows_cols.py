import pandas as pd

people = {
    "first": ["Devesh", "Ankit", "Prince"],
    "last": ["K", "K", "K"],
    "email": ["deveshk237@gmail.com", "deveshk237@gmail.com", "deveshk237@gmail.com"],
}

people_df = pd.DataFrame(people)

# changing the columns to upper case
# people_df = [x.upper() for x in people_df.columns]
# print(people_df)

# renaming some column names
people_df.rename(columns={"first": "first_name", "last": "last_name"}, inplace=True)
print(people_df)

# changing specific row values
people_df.loc[0, ["first_name", "last_name"]] = ["Nandini", "Kumari"]

# we can also use .at() method
people_df.at[
    1,
    "first_name",
] = "Devesh"

# print(people_df)

# using str methods on specific column
people_df["first_name"] = people_df["first_name"].str.lower()

# print(people_df)

# apply method - on series
# print(people_df["email"].apply(len))

people_df["email"] = people_df["email"].apply(lambda x: x.upper())

print(people_df)

# applymap
print(people_df.map(len))

# applying this to stackoverflow dataset

df = pd.read_csv("stack-overflow-developer-survey-2023/survey_results_public.csv")

df.rename(columns={'CompTotal': 'SalaryUSD'}, inplace=True)

print(df.columns)