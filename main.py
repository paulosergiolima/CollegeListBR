from copy import copy
from string import ascii_uppercase as alc
from flask import request, Flask, send_file
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