#!/usr/bin/env python
# coding: utf8
from flask import Flask, jsonify, request
import sys, os
import commands
from controller import moveServo
import threading

class Server:

    app = Flask(__name__)

    @app.route('/')
    def all():
        temp1 = 23.5
        temp2 = 21.2
        ip = request.remote_addr
        callback = request.args.get('callback')
        return '{0}({1})'.format(callback, {'client_ip':ip,'b':2,'temp1':temp1,'temp2':temp2})

    @app.route('/online/')
    def online():
        callback = request.args.get('callback')
        return '{0}({1})'.format(callback, {'online':'true'})

    @app.route('/status/')
    def status():
        callback = request.args.get('callback')
        statusfrom = request.args.get('from')
        if(statusfrom == "stream"):
            response = commands.getstatusoutput('sudo service motion status')
            print response
            if("Active: active (running)" in response):
                print "Camera Stream ist online!"
                return '{0}({1})'.format(callback, {'online':'true'})
            else:
                print "Camera Stream ist offline!"
                return '{0}({1})'.format(callback, {'online':'false'})



    @app.route('/action/')
    def action():
        callback = request.args.get('callback')
        action = request.args.get('action')
        if(action == "stopScript"):
            callback = request.args.get('callback')
            s1.ChangeDutyCycle(0)
            s2.ChangeDutyCycle(0)
            GPIO.cleanup()
            os.system("sudo pkill -9 python")
            return '{0}({1})'.format(callback, {'online':'true'})

        elif(action == "startStream"):
            callback = request.args.get('callback')
            os.system("sudo service motion start")
            print ("Camera Stream gestartet!")
            return '{0}({1})'.format(callback, {'streamstatus':'online'})

        elif(action == "stopStream"):
            callback = request.args.get('callback')
            os.system("sudo service motion stop")
            print ("camera Stream gestoppt")
            return '{0}({1})'.format(callback, {'streamstatus':'offline'})

        elif(action == "psConnect"):
            callback = request.args.get('callback')
            print ("PS3 Server started")
            return '{0}({1})'.format(callback, {'psConnect':'true'})

        else:
            return '{0}({1})'.format(callback, {'Unbekannter Befehl!'})


    @app.route('/cameramove/', methods=['GET'])
    def cameramove():
        callback = request.args.get('callback')
        x = request.args.get('x')
        y = request.args.get('y')
        moveServo(x, y)
        return '{0}({1})'.format(callback, {'status':'success'})

    @app.route('/drive/', methods=['GET'])
    def drive():
        ret_data = {"value": request.args.get('aktion')}
        wert = request.args.get('aktion')
        print wert
        return jsonify(ret_data)

    @app.route('/sensors/', methods=['GET'])
    def sensors():
        temp1 = 23.5
        temp2 = 21.2
        ret_data = {"temp1": temp1, "temp2": temp2}
        return jsonify(ret_data)

    def start(self):
        server = threading.Thread(target=self.startServer(), args = ())
        server.start()

    def startServer(self):
        if __name__ == '__main__':
            app.run(host='0.0.0.0', port=8081, debug=True, threaded=True)
        else:
            print ("__name__ != __main__")
            #app.run(host='0.0.0.0', port=8081, debug=True, threaded=True)
