import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("Original Array:", arr1)
print("Array + 5:", arr1 + 5)
print("Sliced Array:", arr1[1:4])
print("Reshaped 2D Array:\n", arr2.reshape(3, 2))

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 88]
}
df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

print("\nDataFrame Info:")
print(df.info())

print("\nStatistics:")
print(df.describe())

import matplotlib.pyplot as plt

plt.figure()
plt.plot(df['Name'], df['Score'], marker='o')
plt.title('Scores of Students')
plt.xlabel('Name')
plt.ylabel('Score')
plt.grid(True)
plt.show()

plt.figure()
plt.bar(df['Name'], df['Age'], color='orange')
plt.title('Age of Students')
plt.xlabel('Name')
plt.ylabel('Age')
plt.show()

plt.figure()
plt.pie(df['Score'], labels=df['Name'], autopct='%1.1f%%', startangle=90)
plt.title('Score Distribution')
plt.show()
