import pandas as pd

# opening a csv file in pandas
# df = pd.read_csv("stack-overflow-developer-survey-2023/survey_results_public.csv")

# pd.set_option("display.max_columns", 20)
# pd.set_option("display.max_rows", 20)


# # print(df.shape)  # returns a tuple of no of rows and columns
# # print(df.info())  # returns the columns info of the data

# # print(df)

# schema_df = pd.read_csv(
#     "stack-overflow-developer-survey-2023/survey_results_schema.csv"
# )

people = {
    "first": ["Devesh", "Ankit", "Prince"],
    "last": ["K", "K", "K"],
    "email": ["deveshk237@gmail.com", "deveshk237@gmail.com", "deveshk237@gmail.com"],
}

people_df = pd.DataFrame(people)
# print(people_df)

# print(people_df.email)

# print(people_df["email"])  # preferred way to access columns in a dataframe

# accessing multiple columns in dataframe
# people_df[["last", "email"]]

# iloc - allows us to access rows by integer location
print(people_df.iloc[0])  # we can access multiple rows by passing in a list of integers

print(people_df.iloc[[0, 1], 2])

