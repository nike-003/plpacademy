# ------------------------------
# Load UCI Iris Dataset
# ------------------------------

import pandas as pd

# UCI Iris dataset URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Column names from UCI documentation
columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

# Load dataset
try:
    df = pd.read_csv(url, header=None, names=columns)

    print("First 5 rows of Iris dataset:")
    print(df.head())
    print("\nDataset Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
except Exception as e:
    print("Error loading dataset:", e)
# ------------------------------
# Task 2: Basic Data Analysis
# ------------------------------

# Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Median & Standard Deviation
print("\nMedian:")
print(df.median(numeric_only=True))
print("\nStandard Deviation:")
print(df.std(numeric_only=True))

# Group by species and compute mean petal length
print("\nAverage Petal Length by Species:")
print(df.groupby("species")["petal_length"].mean())

# Example Insight
avg_sepal = df.groupby("species")["sepal_length"].mean()
print("\nSpecies ranked by average sepal length:")
print(avg_sepal.sort_values(ascending=False))
# ------------------------------
# Task 3: Data Visualization
# ------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Line Chart – Average Petal Length per Species
plt.figure(figsize=(8,5))
df.groupby("species")["petal_length"].mean().plot(kind="line", marker="o")
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 2. Bar Chart – Average Sepal Width per Species
plt.figure(figsize=(8,5))
df.groupby("species")["sepal_width"].mean().plot(kind="bar", color="skyblue")
plt.title("Average Sepal Width by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Width (cm)")
plt.show()

# 3. Histogram – Distribution of Petal Length
plt.figure(figsize=(8,5))
plt.hist(df["petal_length"], bins=15, color="orange", edgecolor="black")
plt.title("Distribution of Petal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot – Sepal Length vs Petal Length
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df, palette="deep")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
