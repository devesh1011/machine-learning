import pandas as pd

df = pd.read_csv("stack-overflow-developer-survey-2023/survey_results_public.csv")

india_python_dev_df = df[
    (df["Country"] == "India")
    & (df["ConvertedCompYearly"] > 20000)
    & (df["LanguageHaveWorkedWith"].str.contains("Python", na=False))
]

india_python_dev_df.to_csv("../Matplotlib/salary.csv")