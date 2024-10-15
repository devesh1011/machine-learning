# aggregating
import pandas as pd

df = pd.read_csv("stack-overflow-developer-survey-2023/survey_results_public.csv")

# print(df["Country"].value_counts())

country_grp = df.groupby("Country")

# print(country_grp["Industry"].value_counts().loc["India"])

# print(country_grp.get_group("India")["WebframeHaveWorkedWith"].value_counts())

# print(df.loc['ResponseId'].head(10))

filt = df["LanguageHaveWorkedWith"].str.contains("Python", na=False)

filtered_df = df[filt]
filtered_country_grp = filtered_df.groupby("Country")

# either you can use apply method to filter
# print(
#     country_grp["LanguageHaveWorkedWith"]
#     .apply(lambda x: x.str.contains("Python", na=False).sum())
#     .head(50)
# )


# calculating the median salary for each country
# print(filtered_country_grp["ConvertedCompYearly"].median())

# to use multiple functions in the grp
# print(country_grp["ConvertedCompYearly"].agg(["median", "mean"]).head(50))

# challenge - what percentage of people from each country use python


knows_python = country_grp["LanguageHaveWorkedWith"].apply(
    lambda x: x.str.contains("Python", na=False).sum()
)

respondents = df["Country"].value_counts()
# print(respondents)

python_df = pd.concat([respondents, knows_python], sort=False, axis="columns")

python_df.rename(
    columns={"count": "Respondants", "LanguageHaveWorkedWith": "knows_python"},
    inplace=True,
)

python_df["percent knows python"] = (
    python_df["knows_python"] / python_df["Respondants"]
) * 100

python_df.sort_values(by="percent knows python", ascending=False, inplace=True)

print(python_df.head(50))
