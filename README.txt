# Student Grades Prediction with Machine Learning

## Project Overview
This project aims to predict the final grades of students based on their performance in previous periods, study time, failures, and absences. By predicting student grades, instructors can identify students who may need additional support.

## Dataset
The dataset used for this project contains the following columns:
- G1: Grades of the first period
- G2: Grades of the second period
- G3: Final grades (target variable)
- studytime: Weekly study time
- failures: Number of past class failures
- absences: Number of school absences

The dataset is based on the achievements of students in Portuguese schools.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn

## Steps
1. **Data Loading:** Load the dataset.
2. **Data Preprocessing:** Select relevant columns and split data into features and target.
3. **Data Splitting:** Split the data into training and test sets.
4. **Model Training:** Train a linear regression model.
5. **Model Evaluation:** Evaluate the model's accuracy on the test set.
6. **Grade Prediction:** Use the trained model to predict the final grades of students.

## Usage
1. Ensure you have the necessary Python libraries installed:
    ```bash
    pip install pandas numpy scikit-learn
    ```
2. Run the Python script:
    ```bash
    python student_grades_prediction.py
    ```
3. The script will print the model's accuracy and the predicted vs. actual grades for the test set.

## Author
Kishore Sakthivel
