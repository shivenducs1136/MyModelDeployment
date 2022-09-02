import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def marks_prediction(hrs):
    x = pd.read_csv(r'E:\Flask\_Demo\x.csv')
    y = pd.read_csv(r'E:\Flask\_Demo\y.csv')
    
    X = x.values
    Y = y.values

    model = LinearRegression()
    model.fit(X,Y)
    
    X_text = np.array(hrs)
    X_text = X_text.reshape((1,-1))
    return model.predict(X_text)[0]
