from sklearn.svm import SVR
from sklearn.externals import joblib
from sklearn.preprocessing import RobustScaler
import numpy as np
from sklearn.preprocessing import StandardScaler
# load the CSV file as a numpy matrix
def modeling(input) :

    dataset = np.loadtxt("models/First_trial_regression.csv", delimiter=",")
    # separate the data from the target attributes
    X = dataset[:,0:12]
    Y = dataset[:,12]

    rbX = RobustScaler()
    X = rbX.fit_transform(X)

    rbY = RobustScaler()
    Y = np.expand_dims(Y, 0)
    Y = Y.T
    Y = rbY.fit_transform(Y) 

    clf = SVR(C=1.000, epsilon=0.2, kernel="rbf")
    clf.fit(X, Y)

    joblib.dump(clf, 'models/SMOreg.pkl')

    clf2 = joblib.load('models/SMOreg.pkl')


    audience_num = clf2.predict(rbX.transform(input))
    audience_num = np.expand_dims(audience_num,0)
    audience_num = audience_num.T
    audience_num = rbY.inverse_transform(audience_num)

    return audience_num