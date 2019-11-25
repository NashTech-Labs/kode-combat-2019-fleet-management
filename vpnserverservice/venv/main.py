from flask import Flask, request
import subprocess
import os
app = Flask(__name__)


@app.route('/list')
def list_client():
    result = subprocess.check_output(["/bin/bash","-c","/usr/local/bin/vpnlist"])
    return str(result)

@app.route("/addClient")
def add_client():
    uuid = request.args['uuid']
    result = subprocess.check_output(["/bin/bash","-c",f"export MENU_OPTION='1'; export CLIENT='{uuid}'; export PASS='1'; vpnmanager"])
    vpnConf = open(f'/home/knoldus/client-ovpn/{uuid}.ovpn', 'rU').read()
    return vpnConf

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
