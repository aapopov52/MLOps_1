import os
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = load_iris()
X, y = data['data'], data['target']

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size = 0.3, random_state = 42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
print('Модель - запуск обучения')
model.fit(X_train, y_train)
with open('/app/iris_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print('Модель создана')