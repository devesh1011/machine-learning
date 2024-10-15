import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Titanic-Dataset.csv")

# working this categorical data
# sns.countplot(df["Pclass"].value_counts())
# plt.show()

# working with numerical data

# plotting histogram
plt.hist(df["Age"], bins=20, color="skyblue", edgecolor="black", alpha=0.7)

# # Adding title and labels
plt.title("Distribution of Age on the Titanic", fontsize=16)
plt.xlabel("Age", fontsize=14)
plt.ylabel("Frequency", fontsize=14)

# Display the plot
# plt.show()


# displot used to see the probabilty
sns.displot(df["Age"])
plt.show()

# boxplot
# Create a horizontal boxplot
sns.boxplot(x=df["Fare"], color="skyblue")

# Add a title and labels for clarity
plt.title("Distribution of Fare on the Titanic", fontsize=16)
plt.xlabel("Fare", fontsize=14)

# Display the plot
plt.show()
