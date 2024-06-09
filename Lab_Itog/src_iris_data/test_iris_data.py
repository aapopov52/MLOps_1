import os

from fastapi.testclient import TestClient

import pandas as pd



def test_api_find_file():

    assert  os.path.exists("iris_dataset.csv") == True

    

def test_api_isnull():

    df = pd.read_csv("iris_dataset.csv")

    assert  df.isnull().sum() == 0





def test_api_duplicates():

    df = pd.read_csv("iris_dataset.csv")

    assert  df.duplicated().sum() == 0

