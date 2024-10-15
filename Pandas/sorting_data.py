import pandas as pd

people = {
    "first": ["Devesh", "Ankit", "Prince"],
    "last": ["Kumar", "Dalal", "Yadav"],
    "email": ["deveshk237@gmail.com", "deveshk237@gmail.com", "deveshk237@gmail.com"],
}

people_df = pd.DataFrame(people)

# sorting a column
people_df.sort_values(by="first", inplace=True, ascending=False)

# to sort multiple columns we can pass a list of columns in the 'by' parameter

# sorting the dataframe using indexes
people_df.sort_index(inplace=True)

# print(people_df)

# with the real dataset
df = pd.read_csv("stack-overflow-developer-survey-2023/survey_results_public.csv")

df.sort_values(by="CompTotal", inplace=True, ascending=False)
# print(df[["Country", "CompTotal"]].head(50))

print(df.nlargest(10, "CompTotal"))
