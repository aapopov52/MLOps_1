import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def main():

    if not os.path.exists('train'):
        os.makedirs('train')
    if not os.path.exists('test'):
        os.makedirs('test')
    data = np.random.normal(loc=20, scale=5, size=(5000, 5))

    columns = ['fut1', 'fut2', 'fut3', 'fut4', 'anomalies']
    df = pd.DataFrame(data=data, columns=columns)
    df['target'] = 0.1 + df['fut1'] * 2 + df['fut2'] * 3 + \
                         df['fut3'] * 0.5 + df['fut4'] * 2.5
    
    flag = df['anomalies'] < 5
    df.loc[flag, 'fut2'] = df.loc[flag, 'fut2'] + df.loc[flag, 'anomalies'] * 2
    
    flag = df['anomalies'] > 25
    df.loc[flag, 'fut3'] = df.loc[flag, 'fut3'] + df.loc[flag, 'anomalies']
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
    
    columns_save = ['fut1', 'fut2', 'fut3', 'fut4', 'target']
    train_df[columns_save].to_csv('train/train.csv', index=False)
    test_df[columns_save].to_csv('test/test.csv', index=False)

main()

