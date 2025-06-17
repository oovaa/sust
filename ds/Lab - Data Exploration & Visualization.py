#!/usr/bin/env python
# coding: utf-8

# # Data Exploration & Visualization

# ## Impoting The Dataset

# In[1]:


from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = load_iris()
iris_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_data.head(10)


# ## Quantitative Checks

# In[2]:


print("Dataset Shape:", iris_data.shape)
print("_______________________________________________________________")
print("\nColumn Names:", iris_data.columns)
print("_______________________________________________________________")
print("\nData Types:\n", iris_data.dtypes)
print("_______________________________________________________________")
print("\nBasic Statistical Summary:\n", iris_data.describe())
print("_______________________________________________________________")
print(iris_data.isnull().sum())


# ## Summary Statistics Techniques

# In[4]:


print("Frequency Distributions:")
print(iris_data.round(1).apply(lambda x: x.value_counts()).fillna(0))
print("_______________________________________________________________")

# Mode calculation
print("Mode of Each Column:")
print(iris_data.mode().iloc[0])
print("_______________________________________________________________")

# Percentile computations (25th, 50th, 75th)
percentiles = [25, 50, 75]
print("Percentile Computations:")
print(iris_data.quantile(q=np.array(percentiles) / 100))
print("_______________________________________________________________")

# Mean and median calculations
print("Mean Values:")
print(iris_data.mean())
print("\nMedian Values:")
print(iris_data.median())
print("_______________________________________________________________")

# Range (Max - Min)
print("Range of Each Column:")
print(iris_data.max() - iris_data.min())
print("_______________________________________________________________")

# Variance measurements
print("Variance of Each Column:")
print(iris_data.var())


# # Visualization

# ## Pie Chart

# In[ ]:


iris_data["species"] = [iris.target_names[i] for i in iris.target]  # Add species labels

# Count occurrences of each species
species_counts = iris_data["species"].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 6))
plt.pie(species_counts, labels=species_counts.index, autopct="%1.1f%%", colors=["lightblue", "lightgreen", "lightcoral"])

plt.title("Distribution of Iris Species")
plt.show()


# ## Bar Chart

# In[ ]:


mean_values = iris_data.drop(columns=["species"]).mean() 

# Create a bar chart
plt.figure(figsize=(8, 5))
plt.bar(mean_values.index, mean_values.values, color=['blue', 'green', 'red', 'purple'])

# Add labels and title
plt.xlabel("Features")
plt.ylabel("Mean Value")
plt.title("Mean Values of Iris Dataset Features")
plt.xticks(rotation=45)  # Rotate labels for better readability

# Show the plot
plt.show()


# ## Histograms

# In[ ]:


# Create histograms for each feature
iris_data.hist(figsize=(10, 6), bins=20, edgecolor='black')

# Add title
plt.suptitle("Histograms of Iris Dataset Features", fontsize=16)

# Show the plot
plt.show()


# ## Scatter Plots

# In[ ]:


iris_data["species"] = [iris.target_names[i] for i in iris.target]  # Add species labels

# Select two features to plot (e.g., sepal length vs petal length)
x_feature = "sepal length (cm)"
y_feature = "petal length (cm)"

# Create scatter plot
plt.figure(figsize=(8, 6))
for species in iris_data["species"].unique():
    subset = iris_data[iris_data["species"] == species]
    plt.scatter(subset[x_feature], subset[y_feature], label=species)

# Add labels and title
plt.xlabel(x_feature)
plt.ylabel(y_feature)
plt.title(f"Scatter Plot of {x_feature} vs {y_feature}")
plt.legend()
plt.show()


# ## Box Plot

# In[ ]:


import seaborn as sns


iris_data["species"] = [iris.target_names[i] for i in iris.target]  # Add species labels

# Create a box plot for all numerical features grouped by species
plt.figure(figsize=(8, 6))
sns.boxplot(data=iris_data, x="species", y="sepal length (cm)")
plt.title("Box Plot of Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.show()


# In[ ]:




