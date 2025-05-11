import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing

# Step 1: Load the dataset
california_data = fetch_california_housing(as_frame=True)  # ← was "is_frame", should be "as_frame"
data = california_data.frame

# Step 2: Compute the correlation matrix
california_matrix = data.corr()

# Step 3: Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(california_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlation Matrix of California Housing Features")
plt.show()

# Step 4: Create a pair plot
sns.pairplot(data, diag_kind='kde', plot_kws={'alpha': 0.5})
plt.suptitle('Pair Plot of California Housing Features', y=1.02)  # ← was subtitle, should be suptitle
plt.show()
