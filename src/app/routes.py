# -*- coding: utf-8 -*-
from flask import render_template, request, url_for, g
from app import app
from contextlib import closing
import sqlite3
import os
from model import User

basedir = os.path.abspath(os.path.dirname(__file__))


menu = [{'name': u'Главная', 'url': '/'},
        {'name': u'Добавить пост', 'url': '/add_post'},
        {'name': u'Блог', 'url': '/blog'},
        {'name': u'Партнеры', 'url': '/partners'},
        {'name': u'О нас', 'url': '/about'}]


# def connect_db():
#     return sqlite3.connect(app.config['DATABASE'])
#
#
# def init_db():
#     with closing(connect_db()) as db:
#         with app.open_resource('data.sql', mode='r') as f:
#             db.cursor().executescript(f.read())
#         db.commit()
#
# #init_db()
#
# @app.before_request
# def before_request():
#     g.db = connect_db()
#
#
# @app.teardown_request
# def teardown_request(exception):
#     db = getattr(g, 'db', None)
#     if db is not None:
#         db.close()

@app.route("/")
@app.route("/index")
def index():
    title = u'Главная'
    return render_template('index.html', title=title, menu=menu)

@app.route('/blog')
def about():
    title = u'Блог'
    return render_template('blog.html', title=title, menu=menu)

@app.route('/add_post', methods=['POST', 'GET'])
def add_post():
    title = u'Новый пост'
    data_dict = {}

    if request.method == 'POST':
        data_dict['title'] = (request.form['title'])
        data_dict['author'] = (request.form['author'])
        data_dict['text'] = (request.form['text'])
        g.db.execute('insert into entries (title, author, text) values (?, ?, ?)', [request.form['title'], request.form['author'], request.form['text']])
        g.db.commit()

    cur = g.db.execute('SELECT title, author, text FROM entries ORDER BY id DESC')
    entries = [dict(title=row[0], author=row[1], text=row[2]) for row in cur.fetchall()]
    return render_template('add_post.html', title=title, menu=menu, data_dict=data_dict, entries=entries)


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    data_dict = {}
    title = u'Регистрация'
    if request.method == 'POST':
        data_dict['login'] = (request.form['login'])
        data_dict['pass'] = (request.form['pass'])
        data_dict['repeat_pass'] = (request.form['repeat_pass'])
        role = 1
        g.db.execute('insert into users (login, pass, role) values (?, ?, ?)', [request.form['login'], request.form['pass'], '1'])
        g.db.commit()

    return render_template('registration.html', title=title, menu=menu, data_dict=data_dict)



@app.route("/debug")
def debug():

    user = User('dima', '123456')

    return user.show_user()
