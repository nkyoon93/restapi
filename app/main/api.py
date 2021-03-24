from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app

from  app.module import dbModule

api = Blueprint('api', __name__, url_prefix='/test')

@api.route('/', methods=['GET'])
def index():
    return render_template('/api/api.html',
                           result=None,
                           resultData=None,
                           resultUPDATE=None)
@api.route('/insert', methods=['GET'])
def insert():
    db_class = dbModule.Database()
    sql      = "INSERT INTO TESTDB.testTable(test) \"" \
                VALUES('%s')" % ('testData')
    db_class.execute(sql)
    db_class.commit()
    return render_template('/api/api.html',
                           result='insert!',
                           resultData=None,
                           resultUPDATE=None)

@api.route('/select', methods=['GET'])
def select():
    db_class = dbModule.Database()
