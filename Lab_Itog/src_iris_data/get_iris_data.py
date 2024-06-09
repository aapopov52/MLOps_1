import os

import pandas as pd

from sklearn.datasets import load_iris



data = load_iris()

X, y = data['data'], data['target']



df = pd.DataFrame(data.data, columns=data.feature_names)

df['target'] = data.target

df.to_csv('iris_dataset.csv', index=False)
