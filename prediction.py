import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates = []
prices = []

def getData(filename):
    with open(filename,'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        for row in csvFileReader:
            data = row[0]
            values = data.split('-')
            dateValues = values[0].split(':')
            askValue = values[-1]
            askDay = dateValues[3]
            dates.append(int(askDay))
            prices.append(float(askValue))
    return

def predict_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates), 1))
    # print(dates)
    svr_lin = SVR(kernel= 'linear', C=1e3)
    svr_poly = SVR(kernel= 'poly', C=1e3, degree=2)
    svr_rbf = SVR(kernel= 'rbf', C=1e3, gamma=0.1)
    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)
    # print(svr_lin.predict([[x]]))
    # exit()
    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr_rbf.predict(dates), color='red',label='RBF model')
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
    plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support vector regression')
    plt.legend()
    print(svr_rbf.predict([[x]])[0], svr_lin.predict([[x]])[0], svr_poly.predict([[x]])[0])
    plt.show()

    # return svr_rbf.predict([[x]])[0], svr_lin.predict([[x]])[0], svr_poly.predict([[x]])[0]
getData('test.csv')
# print(dates, prices)
predicted_price = predict_prices(dates, prices,19)
print(predicted_price)
