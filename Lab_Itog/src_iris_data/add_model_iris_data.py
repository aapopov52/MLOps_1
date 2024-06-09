import os

import pickle

import pandas as pd

from sklearn.ensemble import RandomForestClassifier



df = pd.read_csv("iris_dataset.csv")



# нам не нужна и тестовая, ни валидационная выборки, поэтому учим по всему

X_train = df[['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']]

y_train = df['target']



model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X_train, y_train)

with open('iris_model.pkl', 'wb') as f:

    pickle.dump(model, f)

print('Модель создана')
