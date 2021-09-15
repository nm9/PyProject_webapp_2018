import matplotlib
from flask import Flask, render_template, request, send_file

matplotlib.use('agg')
from io import BytesIO

import mpld3
from matplotlib import pyplot as plt

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('layout.html')
@app.route('/plot', methods=['GET','POST'])
def plot():
    if request.method=="POST":
        kind=request.form['type']
        
        xpoints=request.form['x-axis']
        l_x=xpoints.split(',')
        ypoints=request.form['y-axis']
        l_y=ypoints.split(',')
        l_x=list(map(int,l_x))
        l_y=list(map(int,l_y))
        plt.figure()
        if kind=="a":            
            plt.plot(l_x,l_y)
        elif kind=="b":
            plt.bar(l_x,l_y)
        elif kind=="c":
            plt.pie(l_x,labels=l_y)
        elif kind=="d":
            plt.hist(l_x,bins=3,label=l_y)
        elif kind=="e":
            plt.scatter(l_x,l_y)
        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        return send_file(img, mimetype='image/png')

if __name__ == '__main__':
  app.run(debug=True)
