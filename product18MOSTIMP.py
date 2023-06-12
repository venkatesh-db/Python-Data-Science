
# Design

import pandas as pd   -> knowing design of the lib & method’s

import numpy as np  -> knowing design of the lib & method’s

import time  -> knowing design of the lib & method’s

# visual libraries
from matplotlib import pyplot as plt  -> knowing design of the lib & method’s

import seaborn as snss

from mpl_toolkits.mplot3d
import Axes3D
plt.style.use('ggplot')


# sklearn libraries
from sklearn.neighbors import KNeighborsClassifier -> knowing design of the lib & method’s

from sklearn.model_selection import train_test_split -> knowing design of the lib & method’s
from sklearn.preprocessing import normalize

from sklearn.metrics import 
confusion_matrix,accuracy_score,precision_score,recal
l_score,f1_score,matthews_corrcoef,classification_report,roc_curve

from sklearn.externals import joblib

from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA

# 200 LOC  { 90% Lib } Program Flow Execution

pca = PCA(n_components=2)
# 7 Method's used only 1method
pca.fit(X)

scaler = StandardScaler()
# 6 method's used only 1method
scaler.fit(data))
print(scaler.mean_)

X_train = np.array([[ 1., -1.,  2.],
                     [ 2.,  0.,  0.],
                     [ 0.,  1., -1.]])
scaler = preprocessing.StandardScaler().fit(X_train)
scaler


joblib.dump(train_mode, "./train_mode.joblib", compress=True)

from ggplot import *

#https://plotnine.readthedocs.io/en/stable/generated/plotnine.ggplot.html#plotnine.ggplot

ggplot(mpg, aes(x='value', color='variable')) + \
    geom_density()

import matplotlib.pyplot as plt

#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html

plt.xticks(pos_1, cor_label['Variables'],rotation='vertical')
plt.ylabel('Correlation')
plt.title('Correlation between price and variables') 
plt.show()

from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

import statsmodels.api as sm


from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet


from math import sqrt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['A'] = le.fit_transform(df.A)


from sklearn import feature_selection
vt = feature_selection.VarianceThreshold(threshold=.2)
vt.fit_transform(df)











