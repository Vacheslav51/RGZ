from flask import Flask, Blueprint, render_template, request, make_response

from menu import menu

app = Flask(__name__)

app.secret_key = '1226'

app.register_blueprint(menu)