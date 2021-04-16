from flask import Flask, render_template, request ,redirect, session

app = Flask(__name__)
app.secret_key = 'clavesecreta' # asignar una clave secreta por motivos de seguridad

# @app.route('/')
# def index():
#     print("*"*20)
#     print("carga contador.html")
#     return render_template("contador.html")


@app.route('/')
def refresh():
    print("Got Post Info")
    # verificar si ya está creada la sesión
    if 'contador' not in session:
        session['contador'] = 0
    session['contador']+=1
    return render_template('/contador.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/counter_plus_two')
def counter_plus_two():
    session['contador']+=1
    return redirect('/')

@app.route('/increment_xtimes', methods = ['POST'])
def increment_xtimes():
    session['contador']+= int(request.form["increment"]) - 1
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)