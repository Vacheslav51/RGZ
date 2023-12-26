from flask import Blueprint, render_template, request, make_response
menu = Blueprint('menu', __name__)

@menu.route('/menu/')
def main():
    return render_template('menu.html')

@menu.route('/login/')
def login():
    return render_template('login.html')

@menu.route('/reg/')
def reg():
    return render_template('reg.html')