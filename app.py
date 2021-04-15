from flask import Flask, render_template, flash, redirect
from config import Config
from forms import LoginForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config.from_object(Config)
bootstrap = Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        }]
    return render_template("index.html", title='Home', user=user, posts=posts)


@app.route('/login', methods=['Get', 'Post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user{}, remember_me={}'.format(form.username.data, form.remember.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run()
