import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report

# Load data
customers = pd.read_excel('Customers.xlsx')
employees = pd.read_excel('Employee.xlsx')
sales = pd.read_excel('sales.xlsx')

# Merge datasets
df = pd.merge(customers, employees, on='Gender', how='left')
df = pd.merge(df, sales, on='Outlet_Location_Type', how='left')

# Display column names and check for missing values
print("Columns:", df.columns.tolist())
print("Missing values:\n", df.isnull().sum())

# Impute missing values
imputer = SimpleImputer(strategy='most_frequent')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Encode categorical variables
label_encoders = {}
for col in df_imputed.columns:
    if df_imputed[col].dtype == 'object':
        le = LabelEncoder()
        df_imputed[col] = le.fit_transform(df_imputed[col])
        label_encoders[col] = le

# Define features and target
X = df_imputed.drop('Target_Column_Name', axis=1)  # Replace with actual target column
y = df_imputed['Target_Column_Name']               # Replace with actual target column

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train classifier
clf = BalancedRandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
