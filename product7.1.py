# OOPS { Product }
# File system File :excel ,Xl ,csv ,Text

# Outcome Dataframe { datastructure object }
# Data cleaning , visualisation plotting
# statisctic modeling

#  New class object {  Dataframe colomun's ,  Machine learning Logistic Regression }
#  randomly select the data from Dataframe
#  Learn from ur data product+customer   { past history 10 year's }
#  teach him if gardenparty if they buy he will price  Logistic
#  predication  50% , 

#https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#sphx-glr-auto-examples-tree-plot-tree-regression-py

x = np.arange(10).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(x, y)
model.predict_proba(x)
model.predict(x)
model.score(x, y)
confusion_matrix(y, model.predict(x))




