import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

# check how big is the data
print(df.shape)

# how does the data look like?
print(df.sample(10))

# what is the data type of cols?
print(df.info())

# are there any missing values?
print(df.isnull().sum())

# how does the data look mathematically?
print(df.describe())

# are there any duplicate values?
print(df.duplicated())

# how is the correlation between cols?
# print(df.corr())