from flask import Blueprint, render_template, url_for, render_template_string

views = Blueprint(__name__, 'views')

@views.route('/', methods=['POST', 'GET'])
def home():
    return render_template("dashboard.html")