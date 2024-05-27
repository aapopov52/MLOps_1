import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

def main():
    df = pd.read_csv('train/train1.csv')
    features = df[['fut1', 'fut2', 'fut3', 'fut4']]
    target = df[['target']]

    model = LinearRegression()

    model.fit( features, target)

    if not os.path.exists('model'):
        os.makedirs('model')
        
    joblib.dump(model, 'model/model.pkl')

main()