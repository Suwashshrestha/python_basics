# Importing the required libraries
import numpy as np
import pandas as pd

# 1. Create a small dataset using Numpy
# Generate random scores for 5 students in 3 subjects (Math, Science, English)
np.random.seed(42)  # For reproducibility
num_students = 5
subjects = ['Math', 'Science', 'English']
scores = np.random.randint(50, 101, size=(num_students, len(subjects)))

# 2. Create a Pandas DataFrame from the Numpy array
df = pd.DataFrame(scores, columns=subjects)

# 3. Add additional columns
# Adding a column for student names (Student_1, Student_2, ...)
df['Student'] = [f'Student_{i+1}' for i in range(num_students)]

# Adding a column for the average score
df['Average'] = df[subjects].mean(axis=1)

# Adding a column to classify students as 'Pass' or 'Fail' based on their average score (>60 is Pass)
df['Status'] = np.where(df['Average'] > 60, 'Pass', 'Fail')

# 4. Display key information
print("--- Dataset ---")
print(df)

print("\n--- Subject Averages ---")
print(df[subjects].mean())

print("\n--- Pass/Fail Counts ---")
print(df['Status'].value_counts())
