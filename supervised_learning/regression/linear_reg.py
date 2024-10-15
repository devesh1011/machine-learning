import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# Load the data
data = pd.read_csv("student_data.csv")

# Extract the features and the target variable
study_time = data["study_time"].values.reshape(-1, 1)
print(study_time)
grade = data["grade"].values.reshape(-1, 1)

# Add an intercept column to the feature matrix (X)
X = np.hstack((np.ones_like(study_time), study_time))


# Define the model function (with a minor correction for theta shape)
def model(X, Y, L, iters):
    m = Y.size  # Number of data points
    theta = np.zeros((X.shape[1], 1))  # Initialize theta with the correct shape

    for i in range(iters):
        y_pred = np.dot(X, theta)
        cost = (1 / (2 * m)) * np.sum(np.square(y_pred - Y))

        d_theta = (1 / m) * np.dot(X.T, y_pred - Y)  # Gradient descent
        theta = theta - L * d_theta

    return theta


# Set the learning rate and number of iterations
learning_rate = 0.01
iterations = 1000

# Train the model
theta = model(X, grade, learning_rate, iterations)

# Predictions using the trained model
custom_study_time = 13.8
custom_X = np.array([1, custom_study_time]).reshape(1, -1)  # Prepare the feature vector

predicted_grade = np.dot(custom_X, theta)

print(
    f"Predicted grade for a student who studies {custom_study_time} hours: {predicted_grade[0][0]}"
)

# Plotting the data and the regression line
plt.scatter(study_time, grade, color="blue", label="Data Points")
plt.plot(study_time, np.dot(X, theta), color="red", label="Regression Line")
plt.xlabel("Study Time")
plt.ylabel("Grades")
plt.title("Linear Regression: Study Time vs Grades")
plt.legend()
plt.show()

print(f"Trained model parameters: \nIntercept: {theta[0][0]}, Slope: {theta[1][0]}")
