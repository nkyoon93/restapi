from flask import Blueprint, request, render_template, flash, redirect
from flask import current_app as current_app
from app.module import dbModule

test = Blueprint('test', __name__, url_prefix='/test')
@test.route('/', methods=['GET'])
def index():
    return render_template('/test/test.html',
                           result=None,
                           resultData=None,
                           resultUPDATE=None)

#INSERT FUNCTION
@test.route('/insert',methods = ['GET'])
def insert():
    db_class = dbModule.Database()
    sql      = "INSERT TO DB.testTable(test) \
                VALUES('%s')" % ('testData')
    db_class.execute(sql)
    db_class.commit()

    return render_template('/test/test.html',
                           result=None,
                           resultData=None,
                           resultUPDATE=None)

#SELSCT Function
@test.route('/select', methods=['GET'])
def select():
    db_class = dbModule.Database()
    sql      = "SELECT idx, test \
                FROM testDB.testTable"
    row      = db_class.executeAll(sql)
    print(row)

    return render_template('/test/test.html',
                           result=None,
                           resultData=None,
                           resultUPDATE=None)