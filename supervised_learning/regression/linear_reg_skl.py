import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
import seaborn as sns

# from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

df = load_diabetes()
data = pd.DataFrame(df.data)
data.columns = df.feature_names

X = data
y = df.target

# train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
# print(X_train)

# standardizing the dataset
# scalar = StandardScaler()
# X_train = scalar.inverse_transform(X_train)
# print(X_train)
# X_test = scalar.transform(X_test)

# cross validation
regression = LinearRegression()
regression.fit(X_train, y_train)

cv_scores = cross_val_score(regression, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
mse_scores = -cv_scores  # Convert negative MSE to positive
mean_mse = np.mean(mse_scores)
print(f"Cross-validation MSE: {mean_mse:.2f}")

# Make predictions on the test set
y_pred = regression.predict(X_test)
print(y_pred)

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Values")
plt.show()
