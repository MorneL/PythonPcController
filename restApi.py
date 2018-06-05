from flask import Flask, jsonify, render_template, url_for
from flask_cors import CORS, cross_origin
import webbrowser
import pyautogui 

currentMouseX, currentMouseY = pyautogui.position() 

facebookurl = 'http://www.facebook.com/'
googleurl = 'http://www.google.com/'
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def controlsPage():
    # url_for('static', filename='jquery-3.2.1.min.js')
    print("controls page")
    return render_template('controls.html')

@app.route('/mouse/up', methods=['GET'])
def mouseUp():
    print("mouse move up")
    pyautogui.moveRel(None, -10) 
    return "hi"

@app.route('/mouse/left', methods=['GET'])
def mouseLeft():
    print("mouse move left")
    pyautogui.moveRel(-10, None) 
    return ""

@app.route('/mouse/right', methods=['GET'])
def mouseRight():
    print("mouse move right")
    pyautogui.moveRel(10, None) 
    return ""

@app.route('/mouse/down', methods=['GET'])
def mouseDown():
    print("mouse move down")
    pyautogui.moveRel(None, 10) 
    return ""

@app.route('/mouse/click', methods=['GET'])
def mouseClick():
    print("mouse click")
    pyautogui.click()
    return ""

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='6100')