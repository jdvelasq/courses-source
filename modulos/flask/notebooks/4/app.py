
#---------------------------------------------------------------------------
#
# Datos
# 
import pandas as pd

import io

data = [[45939, 21574, 2876, 1815, 1646,   89,  555],
        [60423, 29990, 4708, 2568, 2366, 1411,  733],
        [64721, 32510, 5230, 2695, 2526, 1546,  773],
        [68484, 35218, 6662, 2845, 2691, 1663,  836],
        [71799, 37598, 6856, 3000, 2868, 1769,  911],
        [76036, 40341, 8220, 3145, 3054, 1905, 1008],
        [79831, 43173, 9053, 3338, 3224, 2005, 1076]]

data = pd.DataFrame(
    data = data,
    index = [1951, 1956, 1957, 1958, 1959, 1960, 1961],
    columns = ['N.Amer', 'Europe', 'Asia', 'S.Amer', 'Oceania', 'Africa', 'Mid.Amer']
)
#---------------------------------------------------------------------------

from flask import Flask, request, flash, render_template, g, session, send_file
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

import matplotlib.pyplot as plt


@app.route('/', methods=['GET', 'POST'])           
@app.route('/index', methods=('GET', 'POST'))
def index():

    session['selected'] = data.columns.tolist()[0]
    
    if request.method == 'POST':
        session['selected'] = request.form['region']
        flash(session['selected'])
        
    return render_template(
        'index.html', 
        regions=data.columns.tolist(), # nombres de las regiones
        selected=session['selected'])  # columna seleccionada)


@app.route('/plot0', methods=['GET'])
def plot0():

    selected = session['selected']
    
    plt.clf()
    plt.bar(
        x = list(data.index),
        height = data[selected])
    plt.title(selected)
    
    plot_obj = io.BytesIO()
    plt.savefig(plot_obj, format='png')
    plot_obj.seek(0)

    return send_file(
        plot_obj,
        attachment_filename='plot.png',
        mimetype='image/png')


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.run(host='0.0.0.0', debug=True)
