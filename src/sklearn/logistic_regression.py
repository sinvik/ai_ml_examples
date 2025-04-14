import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 1: Load dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Labels

# Step 2: Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Step 4: Evaluate the model on test data
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on test data: {accuracy:.2f}")

# Step 5: Save the trained model to a file
joblib.dump(model, 'iris_model.pkl')
print("Model saved as 'iris_model.pkl'")

# Step 6: Load the saved model
loaded_model = joblib.load('iris_model.pkl')

# Step 7: Verify the loaded model by predicting again on the test set
y_pred_loaded = loaded_model.predict(X_test)
accuracy_loaded = accuracy_score(y_test, y_pred_loaded)
print(f"Accuracy with loaded model: {accuracy_loaded:.2f}")

# Step 8: Use the loaded model to predict new data
new_data = [[5.1, 3.5, 1.4, 0.2]]  # Example: new flower's measurements
prediction = loaded_model.predict(new_data)
print(f"Predicted class for new data: {prediction[0]}")
