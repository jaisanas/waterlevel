import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import StandardScaler
import copy
import seaborn as sns
import tensorflow as tf
from sklearn.linear_model import LinearRegression
import pickle

def testpypy(day, month):
    # filename = 'gpr_model.sav'
    # loaded_model = pickle.load(open(filename, 'rb'))
    # sprint_test = np.array([[26,21,14,35,11]])
    # predicted_values = loaded_model.predict(sprint_test)
    # print(predicted_values)

    filename = 'hd_bintang_ninggi1.sav'
    bintang_ninggi_loaded_model = pickle.load(open(filename, 'rb'))
    bintang_ninggi_test = np.array([[day, month]])
    bintang_ninggi_predicted_values = bintang_ninggi_loaded_model.predict(bintang_ninggi_test)
    print(bintang_ninggi_predicted_values[0][0])

    filename = 'model_teluk_siwak1.sav'
    teluk_siwak_loaded_model = pickle.load(open(filename, 'rb'))
    teluk_siwak_test = np.array([[day, month]])
    teluk_siwak_predicted_values = teluk_siwak_loaded_model.predict(teluk_siwak_test)
    print(teluk_siwak_predicted_values[0][0])
    print("jais")
    return [bintang_ninggi_predicted_values[0][0], teluk_siwak_predicted_values[0][0]]

def testpypy2(day, month):
    filename = 'model_bintang_ninggi2.sav'
    bintang_ninggi_loaded_model = pickle.load(open(filename, 'rb'))
    bintang_ninggi_test = np.array([[day, month, 1,1,1,1,1,1,5,1,1,-2.4,-0.7,0,0.3,-12.7,0.1]])
    bintang_ninggi_predicted_values = bintang_ninggi_loaded_model.predict(bintang_ninggi_test)
    print(bintang_ninggi_predicted_values[0][0])

    filename = 'model_teluk_siwak2.sav'
    teluk_siwak_loaded_model = pickle.load(open(filename, 'rb'))
    teluk_siwak_test = np.array([[day, month,1,1,1,1,1,1,5,1,1,-2.4,-0.7,0,0.3,-12.7,0.1]])
    teluk_siwak_predicted_values = teluk_siwak_loaded_model.predict(teluk_siwak_test)
    print(teluk_siwak_predicted_values[0][0])
    print("jais")
    return [bintang_ninggi_predicted_values[0][0], teluk_siwak_predicted_values[0][0]]

