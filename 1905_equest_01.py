from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime
from loginform import LoginForm  
from flask import Flask, render_template, redirect
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login3')
def login3():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    users = db_sess.query(User).filter(User.id > 1)
    return render_template('index2.html', new=users)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')