# Exercise 4: Python Functions

Date: 21-10-2025

Group members:
- Mariajosé Argote
- Maria Victoria Suriel
- Elvis Casco

In this exercise we practiced functions.

The results of the questions 1 to 4 are in the file `hw4_solutions.py`.

This repository creates a library structure to do the following steps (using a `.py` file, containing functions with the same name) to perform data analysis from a CSV file.

All the operations with the functions can be revised in the file `exercise6.ipynb`.

All the functions to operate the library are in the folder process_data; this folder contains the structure to operate all functions inside a library called "process_data".

The structure of the library can be seen in the file `library_structure.txt`.

a. `data_loader.py`: Loads the data.

b. `data_split.py`: Splits the data between train and test.

c. `data_remove_nans.py`: Removes those rows that contain NaN values in the columns: age, gender, ethnicity.

d. `data_fill_nans.py`: Fills NaN with the mean value of the column in the columns: height, weight.

e. `data_encoding.py`: Generates dummies for ethnicity column (One hot encoding).

f. `data_binary.py`: Create a binary variable for gender M/F.

g. & h. `data_train_model.py`: Trains a model in the train data, using as features the columns: 'age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure', 'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis'. It also use as target the column: 'diabetes_mellitus'. After training the model with the train data, it predicts the targets for both the train and test sets and add the prediction as a new column (uses predict_proba from the model to get the predicted probabilities); the new column is called 'predictions'.

i. `data_metrics.py`: Computes the train and test roc_auc metric using roc_auc_score from sklearn.
