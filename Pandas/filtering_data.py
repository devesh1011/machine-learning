import pandas as pd

df = pd.read_csv(
    "stack-overflow-developer-survey-2023/survey_results_public.csv",
    index_col="ResponseId",
)

countries = ["United States of America", "India", "Canada", "Australia"]

high_salary = df["ConvertedCompYearly"] > 200000

sorted_high_salary = df.loc[
    high_salary, ["LanguageHaveWorkedWith", "ConvertedCompYearly"]
].sort_values(by="ConvertedCompYearly", ascending=True)

print(df.loc[high_salary, ["Country", "ConvertedCompYearly"]])

# print(sorted_high_salary)

# filtering on multiple parameters in the data


country_salary = df["Country"].isin(countries)

# print(df.loc[country_salary, "Country"])

# filter the results based on the column that contains a specific string
filt = df["LanguageHaveWorkedWith"].str.contains("Python", na=False)

print(df.loc[filt, "LanguageHaveWorkedWith"])
