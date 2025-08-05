import pandas as pd
from sklearn.linear_model import LogisticRegression
import mlflow
import mlflow.sklearn
import os

print("--- Training Script Started ---")
DATA_PATH = os.path.join('MLProject', 'heart_disease_preprocessing', 'train_processed.csv')

if not os.path.exists(DATA_PATH):
    print(f"ERROR: Training data not found at {DATA_PATH}")
    exit(1)

train_df = pd.read_csv(DATA_PATH)
X_train = train_df.drop('target', axis=1)
y_train = train_df['target']
print(f"Loaded training data with {X_train.shape[0]} samples.")

with mlflow.start_run():
    print("Inside MLflow run. Training model...")
    
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    mlflow.sklearn.log_model(model, "model")
    
    print("Model trained and logged successfully.")

print("--- Training Script Finished ---")