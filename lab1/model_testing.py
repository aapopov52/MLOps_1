import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import joblib


def main():
    model = joblib.load('model/model.pkl')

    df_test = pd.read_csv('test/test.csv')

    features_test = df_test[['fut1', 'fut2', 'fut3', 'fut4']]
    target_test = df_test[['target']]

    target_pred = model.predict(features_test)

    mse = mean_squared_error(target_test,target_pred)
    mae = mean_absolute_error(target_test,target_pred)
    r2 = r2_score(target_test,target_pred)
    
    print('mse:', mse)
    print('mae:', mae)
    print('r2:', r2)


main()