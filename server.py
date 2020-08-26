from flask import Flask, render_template, url_for, request, redirect, make_response
from werkzeug.utils import secure_filename
import secrets
import os
import tempfile

#Global variables, terrible... I know, we'll add a database for these things
summary_forms = {}

#Constants
UPLOAD_FOLDER = '/home/jeff/Documents/Programming/dlvr.gh/static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
no_cache = {"Cache-Control": "no-store"}

#Util functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#init
app = Flask(__name__)

#CONFIG
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#routes
@app.route('/')
@app.route('/landing_page')
def landing_page():
    return render_template("landing_page.html"), no_cache

@app.route('/delivery_mode/<mode>')
def delivery_mode(mode):
    implemented_modes = ['motor', 'tricycle', 'truck']
    if mode in implemented_modes:
        return render_template("motor_page.html", mode=mode), no_cache
    else:
        return "Not Implemented, We'll add it later"

@app.route('/summary_page', methods=['GET', 'POST'])
def summary_page():
    if request.method == 'POST':
        global summary_forms
        current_form = secrets.token_urlsafe(8)
        summary_forms[current_form] = {}
        #print(request.form)
        #return render_template("summary_page.html"), no_cache
        #to prevent the resubmission problem,
        #we need to save the post data somewhere
        summary_forms[current_form]["request_form"] = request.form
        summary_forms[current_form]["request_files"] = {}

        #first ensure that file exists
        source_photo = request.files.get('source_photo', None)
        dest_photo = request.files.get('dest_photo', None)
        if source_photo and \
           not source_photo.filename == "" and\
           allowed_file(source_photo):
            source_photo_file = tempfile.mkstemp(dir=app.config['UPLOAD_FOLDER'])
            summary_forms[current_form]["request_files"]["source_photo"] = source_photo_file.name

        if dest_photo and \
           not dest_photo.filename == "" and\
           allowed_file(dest_photo):
            dest_photo_file = tempfile.mkstemp(dir=app.config['UPLOAD_FOLDER'])
            summary_forms[current_form]["request_files"]["dest_photo"] = dest_photo_file.name
            

        #and feed it to the summary_page
        #and redirect to the summary_page
        return redirect(url_for('summary_page', formid=current_form))
    mode = "GET request"
    return render_template("summary_page.html", summary_forms=summary_forms), no_cache

@app.route('/tracker')
def tracker():
    return render_template("tracker_page.html"), no_cache

@app.route('/handle_form', methods=["POST"])
def handle_form():
    #the only reason for creating this endpoint is to take the form,
    #and send it straight to the summary_page using a get request
    pass
