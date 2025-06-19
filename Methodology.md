# Methodology

## Objective

To build a classification model using Balanced Random Forest to handle imbalanced data after merging multiple datasets, preprocessing, and feature engineering.

---

## 1. Data Collection

Three separate Excel files were used:

- `Customers.xlsx`: Contains customer information.
- `Employee.xlsx`: Contains employee details.
- `Sales.xlsx`: Contains sales-related data.

---

## 2. Data Merging

- The datasets were merged using appropriate keys:
  - `Customers` and `Employees` were merged on the `Gender` column.
  - The resulting dataset was merged with `Sales` on the `Outlet_Location_Type` column.

- Merging was done using left joins to retain as much data as possible.

---

## 3. Data Preprocessing

- **Missing Values Handling**:
  - Missing values were imputed using the `most_frequent` strategy (mode imputation), ensuring that no rows were dropped.
  - `SimpleImputer` from `sklearn.impute` was used.

- **Categorical Encoding**:
  - All categorical variables were label encoded using `LabelEncoder` from `sklearn.preprocessing`.
  - This converted string labels into numeric form required for machine learning models.

---

## 4. Feature Selection

- The final feature matrix `X` was created by dropping the target column from the imputed dataset.
- The target variable `y` was assigned to the specific column to be predicted.
- The target column name needs to be replaced by the actual column (manually updated by the user).

---

## 5. Data Splitting

- The dataset was split into training and testing sets using an 80-20 ratio.
- `train_test_split` from `sklearn.model_selection` was used with a fixed `random_state=42` for reproducibility.

---

## 6. Model Training

- A `BalancedRandomForestClassifier` from `imblearn.ensemble` was used.
- This model combines random undersampling of the majority class with Random Forest training.
- `n_estimators=100` was used with a fixed random state.

---

## 7. Model Evaluation

- Predictions were made on the test data.
- Model performance was evaluated using:
  - Accuracy Score
  - Classification Report (Precision, Recall, F1-score)
- Metrics were printed for performance assessment.

---

## 8. Tools & Libraries

- **Python 3.x**
- **Pandas** for data manipulation
- **NumPy** for numerical operations
- **Scikit-learn** for preprocessing, splitting, and evaluation
- **imbalanced-learn (imblearn)** for Balanced Random Forest
- **openpyxl** for reading Excel files

---




---

## Author

Shivam Sharma

