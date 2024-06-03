from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')


@app.route('/cosas')
def mostrarLenguajes():
    return render_template('cosas.html')


@app.route('/contactos')
def contacto():
    return render_template('contactos.html')


if __name__ == '__main__':
    app.run(debug=True)