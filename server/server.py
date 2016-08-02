#!/usr/bin/env python
# coding: utf8

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.php')

@app.route('/online/')
def online():
    ret_data = {"value": request.remote_addr}
    return jsonify(ret_data)

@app.route('/camera/', methods=['GET'])
def camera():
    ret_data = {"value": request.args.get('aktion')}
    wert = request.args.get('aktion')

    if(wert == "left"):
        print "Kamera links"

    elif(wert == "up"):
        print "Kamera hoch"

    elif(wert == "right"):
        print "Kamera rechts"

    elif(wert == "down"):
        print "Kamera runter"

    elif(wert == "stop-left" or wert == "stop-right"):
        print "Resete X Achse"

    elif(wert == "stop-up" or wert == "stop-down"):
        print "Resete Y Achse"

    else:
        print "Unbekannter Befehl: " + str(wert)

    return jsonify(ret_data)

@app.route('/cameramove/', methods=['GET'])
def cameramove():
    ret_data = {"value": request.args.get('x')}
    x = request.args.get('x')
    y = request.args.get('y')
    print "Maus: " + str(x) + "  " + str(y)

    return jsonify(ret_data)

@app.route('/drive/', methods=['GET'])
def drive():
    ret_data = {"value": request.args.get('aktion')}
    wert = request.args.get('aktion')
    print wert
    return jsonify(ret_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)
