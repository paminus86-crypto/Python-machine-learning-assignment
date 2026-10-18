import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

hours_studied = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
exam_scores = [30, 40, 45, 55, 65, 70, 80, 85, 90, 95]

X = np.array(hours_studied)
y = np.array(exam_scores)

model = LinearRegression()

model.fit(X, y)

try:
    user_hours = float(input("Enter hours studied: "))
    
    predicted_score = model.predict([[user_hours]])
    
    print(f"Predicted exam score: {predicted_score[0]:.2f}")

    plt.scatter(X, y, color='blue', label='Actual Data')
    plt.plot(X, model.predict(X), color='red', label='Regression Line')
    
    plt.scatter([user_hours], [predicted_score[0]], color='green', marker='*', s=150, label='Your Prediction')
    
    plt.title('Study Hours vs Exam Score')
    plt.xlabel('Hours Studied')
    plt.ylabel('Exam Score')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

except ValueError:
    print("Please enter a valid number for hours studied.")