import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing

data=fetch_california_housing(as_frame=True)
housing=data.frame

numerical_features=housing.select_dtypes(include=[np.number]).columns

