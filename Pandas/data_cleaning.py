import pandas as pd

df = pd.read_csv("stack-overflow-developer-survey-2023/survey_results_public.csv")

# dropna is used to remove Nan values from the dataframe. how-all: only those rows will be removed in which all the entries are NaN in a row
df.dropna(axis="index", how="all", inplace=True)

print(df)
