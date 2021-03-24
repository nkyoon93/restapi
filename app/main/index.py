#2nd script for main page


from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

main = Blueprint('main', __name__, url_prefix='/') #how define nae, URL is after /

@main.route('/main', methods=['GET']) #define route in file
def index():
    testData = 'testData array' #data to HTML file

    return render_template('/main/index.html', testDataHtml = testData) #<- same as /project_name/app/templates/main/index.html