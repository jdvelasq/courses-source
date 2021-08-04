
import json
import pickle

from flask import Flask, flash, render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "you-will-never-guess"

# Nombres de las clases
classnames = ["setosa", "versicolor", "virginica"]

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        # Lee los valores de las cajas de texto de la interfaz
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])

        X = [[sepal_length, sepal_width, petal_length, petal_width]]

        with open("clf.pickle", "rb") as f:
            clf = pickle.load(f)

        result = classnames[clf.predict(X)[0]]

    else:
        result = ""

    return render_template("index.html", result=result)


###############################################################
#
# API
#
###############################################################
@app.route("/api/clasify", methods=["GET"])
def classify():
    if "values" in request.args:
        X = request.args["X"]
        X = X.split(",")
        X = [float(v) for v in X]
        X = [X]
        
        with open("clf.pickle", "rb") as f:
            clf = pickle.load(f)

        result = classnames[clf.predict(X)[0]]
        return result
    
    else:
        return "Error: No values field provided."

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
