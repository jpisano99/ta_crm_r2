from my_app import app
from flask import render_template, flash, redirect, url_for, request, session,jsonify
from my_app.cascade_select import *
import json
import logging
import sys

# User Passwords kept here
from my_app import my_secrets

# logging.basicConfig(level=logging.DEBUG)
print ('hello from views')


@app.route('/', methods=['GET', 'POST'])
def login():
    print ("request is a",request.method)
    print ("Looking for: ",url_for('static',filename='images/ta_logo.png'))
    if request.method == 'POST':
        session.pop('user', None)

        if request.form['password'] == my_secrets.passwords["USER_PASSWORD"]:
            print('found password')
            session['user'] = request.form['username']
            return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/index')
def index():
    # Check in on a DB here
    my_ver = sys.version
    logging.debug(app)
    return render_template('basic_index.html',my_ver = my_ver)


@app.route('/cascade_select' ,methods=['GET','POST'])
def cascade_select():
    if request.method == 'POST':
        hierarchy = json.loads((request.data).decode("utf-8"))
        levelArray = build_sales_list(hierarchy)
        return jsonify({'levels': levelArray})
    else:
        return render_template('cascade_select.html')

@app.route('/line_items/<int:page_num>')
def line_items(page_num):
    # Display db rows with options for delete/edit/email
    # Sourced from YouTube pagination example
    # https://www.youtube.com/watch?v=hkL9pgCJPNk
    details = Coverage.query.paginate(per_page=6,page=page_num,error_out=True)
    print ('query result',details)
    return render_template('line_items.html',details=details,my_name='any')


@app.route('/modify/<string:action>/<int:id>', methods=['GET', 'POST'])
def modify(action,id):
    record = Coverage.query.filter(Coverage.id == id)
    if action == 'delete':
        action = ['delete','Delete this ?']
    elif action == 'mail':
        action =  ['mail','Mail This ?']
    elif action == 'edit':
        action = ['edit','Save Changes ?']

    print("Action request :",action,record[0].id,record[0].pss_name)

    return render_template('modify.html', record=record,action=action)


@app.route('/saveit/<int:id>',methods=['GET', 'POST'])
def saveit(id):
    if request.method == 'POST':
        record = Coverage.query.filter(Coverage.id == id)
        action = request.form['btnClick']
        print("Action taken :", action, record[0].id, record[0].pss_name)
        if action == 'edit':
            record[0].pss_name = request.form['pss_name']
            record[0].tsa_name = request.form['tsa_name']
            record[0].sales_level_1 = request.form['sales_level_1']
            record[0].sales_level_2 = request.form['sales_level_2']
            record[0].sales_level_3 = request.form['sales_level_3']
            record[0].sales_level_4 = request.form['sales_level_4']
            record[0].sales_level_5 = request.form['sales_level_5']
            record[0].fiscal_year = request.form['fiscal_year']
            db.session.commit()
        elif action == 'delete':
            names = Coverage.query.filter(Coverage.id == id).delete()
            db.session.commit()
        elif action == 'mail':
            pass

    return render_template('index.html')

#
# Error handling pages
#


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'),500