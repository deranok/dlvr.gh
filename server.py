from flask import Flask, render_template, url_for, request
app = Flask(__name__)


no_cache = {"Cache-Control": "no-store"}
@app.route('/')
@app.route('/landing_page')
def landing_page():
    return render_template("landing_page.html"), no_cache

@app.route('/delivery_mode/<mode>')
def delivery_mode(mode):
    implemented_modes = ['motor', 'tricycle', 'truck']
    if mode in implemented_modes:
        return render_template("motor_page.html"), no_cache
    else:
        return "Not Implemented, We'll add it later"

@app.route('/summary_page', methods=['GET', 'POST'])
def summary_page():
    return render_template("summary_page.html"), no_cache

@app.route('/tracker')
def tracker():
    return render_template("tracker_page.html"), no_cache
