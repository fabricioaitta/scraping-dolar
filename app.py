from flask import Flask, render_template
import dolar

app = Flask(__name__, template_folder='template')

@app.route("/")

def index():
    return render_template("index.html", pc=dolar.decimeDolar(), pv=dolar.decimeDolarVenta())

if __name__ == "__main__":
    app.run(debug=True, port=3003)