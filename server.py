from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html",numb=3,color="lightblue")	# notice the 2 new named arguments!

@app.route('/play/<int:numb>')
def change_numb(numb):
    return render_template("index.html",numb=numb,color="lightblue")	# notice the 2 new named arguments!

@app.route('/play/<int:numb>/<color>')
def change_col(numb,color):
    return render_template("index.html",numb=numb,color=color)	# notice the 2 new named arguments!


if __name__=="__main__":
    app.run(debug=True)

