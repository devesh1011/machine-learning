import pandas as pd

# df = pd.read_csv("stack-overflow-developer-survey-2023/survey_results_public.csv")

people = {
    "first": ["Devesh", "Ankit", "Prince"],
    "last": ["K", "K", "K"],
    "email": ["deveshk237@gmail.com", "deveshk237@gmail.com", "deveshk237@gmail.com"],
}

people_df = pd.DataFrame(people)

people_df["full_name"] = people_df["first"] + " " + people_df["last"]

# removing columns from a dataset
print(people_df.drop(columns=["first", "last"], inplace=True))

people_df[["first", "last"]] = people_df["full_name"].str.split(" ", expand=True)

# print(people_df)

# add a single row of data
new_row = pd.DataFrame({"first": ["Tony", "Captain"], "last": ["Stark", "America"]})

people_df = pd.concat([people_df, new_row], ignore_index=True)

# removing rows from data
people_df.drop(index=4, inplace=True)

print(people_df)
