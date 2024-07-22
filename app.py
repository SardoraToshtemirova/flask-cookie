from flask import Flask,render_template,request,redirect,make_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome/',methods=['POST'])
def welcome():
    name = request.form['name']
    email = request.form['email']


    response = make_response(redirect('/Login'))
    response.set_cookie('user_name',name)
    response.set_cookie('user_email',email)

    return response

@app.route('/Login')
def greet():
    user_name = request.cookies.get('user_name')
    if user_name:
        return render_template('Login.html',name=user_name)
    return redirect('/')


@app.route('/logout')
def logout():
    response = make_response(redirect('/'))

    response.delete_cookie('user_name')
    response.delete_cookie('user_email')
    return response


if __name__ == '__main__':
    app.run(debug=True)