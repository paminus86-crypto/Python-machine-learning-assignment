Python Machine Learning Practical Assignment

Name: Paminus Nyamweya
Project Title: Supervised and Unsupervised Machine Learning

Project Descriptions

Supervised Learning Project (Student Exam Score Prediction):
This project uses Linear Regression to predict exam scores based on hours studied. It prepares data using Python lists, trains a model using Scikit-learn's fit() method, takes user input for study hours, and predicts the score using predict(). The prediction is rounded to two decimal places. As a bonus, Matplotlib is used to graph the relationship between study hours and scores, including the user's prediction point.

Unsupervised Learning Project (Customer Segmentation):
This project uses K-Means Clustering to group supermarket customers based on their monthly spending and visits. The data is prepared in a Python list and scaled using StandardScaler. A K-Means model is created with 3 clusters, a random state of 42, and an n_init of 10. The program displays the cluster assigned to each customer and the total number of customers in each cluster. As a bonus, Matplotlib is used to display the customer groups in different colors.

Installation and Running Instructions

1. Install the required dependencies:
   pip install -r requirements.txt

2. Run the supervised machine learning script:
   python supervised_ml.py

3. Run the unsupervised machine learning script:
   python unsupervised_ml.py


Theory Questions

1. What is supervised machine learning?
Supervised machine learning is a type of machine learning where the model is trained on a labeled dataset. The training data includes both the input features and the correct target output. The algorithm learns the mapping function from inputs to outputs, allowing it to predict the output for new data.

2. What is unsupervised machine learning?
Unsupervised machine learning is a type of machine learning where the model is trained on unlabeled data. The algorithm is not given any correct answers. Instead, its goal is to discover hidden patterns, structures, or relationships within the data on its own.

3. Explain the difference between supervised and unsupervised learning.
The primary difference lies in the training data. Supervised learning uses labeled data (input-output pairs) and aims to predict a specific target. Unsupervised learning uses unlabeled data (only inputs) and aims to find underlying structures or groupings within the data.

4. Why is Linear Regression considered supervised learning?
Linear Regression is considered supervised learning because it requires a labeled dataset to train. It learns by comparing its predicted values against the actual known target values provided in the training data, adjusting itself to minimize the error.

5. Why is K-Means considered unsupervised learning?
K-Means is considered unsupervised learning because it does not require a labeled target variable. It analyzes the input data and groups similar data points together into clusters based solely on the distance between them, discovering patterns without being told what the groups should be.

6. What is the difference between fit() and predict()?
fit() is used to train the model. It takes the training data and adjusts the model's internal parameters to learn from the data.
predict() is used to infer outputs after the model has been trained. It takes new, unseen input data and uses the learned parameters to generate predictions.

7. Give two real-world applications of supervised learning and two of unsupervised learning.
Supervised Learning Applications:
1. Spam Filtering: Predicting whether an email is spam based on past labeled examples.
2. Medical Diagnosis: Predicting if a patient has a disease based on historical patient data.

Unsupervised Learning Applications:
1. Customer Segmentation: Grouping customers with similar buying habits for marketing.
2. Anomaly Detection: Identifying unusual patterns in financial transactions that might indicate fraud.