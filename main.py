from flask import request, Flask, send_file, render_template, url_for
from college_workbook import create
app = Flask(__name__)
@app.route('/<path:year>/<path:type>/<path:raw_courses>', methods=['POST', 'GET'])
def login(year, type, raw_courses):
    raw_courses = raw_courses.replace('_', ' ')
    courses = raw_courses.split(';')
    print(courses)
    print(raw_courses)
    file = create(type=type, year=year, courses=courses)
    return send_file(file)
@app.route('/')
def index():
    return render_template('index.html')
