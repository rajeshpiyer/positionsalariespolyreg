from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        import os
        import pandas as pd
        import numpy as np

        dataset = pd.read_csv("Position_Salaries.csv")
        x = dataset.iloc[:, 1]
        y = dataset.iloc[:, 2]

        from sklearn.preprocessing import PolynomialFeatures
        X = x.values.reshape(-1, 1)
        poly = PolynomialFeatures(degree=4)
        X_poly = poly.fit_transform(X)
        poly.fit(X_poly,y)
    
        from sklearn.linear_model import LinearRegression
        regressor = LinearRegression()
        regressor.fit(X_poly,y)

        y_pred = regressor.predict(X_poly)

        form_data = request.form

        input1 = form_data.get("level")
        Xnew = [[0,0,0,0,input1]]
        result = regressor.predict(Xnew)
        value = result.tolist()

        final="The Predicted salary is" + str(value[0])
        return final

    else:
         return render_template("form.html")

if __name__=='__main__':
   app.run()
