import pandas as pd
from sklearn.preprocessing import StandardScaler


def main():
    df = pd.read_csv('train/train.csv')

    scaler = StandardScaler()
    df1_np = scaler.fit_transform(df)
    df1 = pd.DataFrame(data=df1_np, columns=df.columns)
    
    df1.to_csv('train/train1.csv', index=False)


    df = pd.read_csv('test/test.csv')

    df1_np = scaler.transform(df)
    df1 = pd.DataFrame(data=df1_np, columns=df.columns)
    df1.to_csv('test/test1.csv', index=False)


main()