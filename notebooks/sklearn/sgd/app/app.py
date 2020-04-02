
import pickle

from flask import Flask, request, flash, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=("GET", "POST"))
def index():

    if request.method == 'POST':
        # Nombres de las clases
        classnames = ['setosa', 'versicolor', 'virginica']
        
        # Lee los valores de las cajas de texto de la interfaz
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])

        X = [[sepal_length, sepal_width, petal_length, petal_width]]

        with open("clf.pickle", "rb") as f:
            clf = pickle.load(f)

        result = classnames[ clf.predict(X)[0] ]
        
    else:
        result = ''

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
