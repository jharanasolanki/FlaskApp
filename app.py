# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:42:26 2021

@author: Lenovo
"""
import SocketServer
import struct

from flask import Flask
app = Flask(__name__)
@app.route("/")
def main():
    return "Welcome!"
if __name__ == "__main__":
    HOST, PORT = "localhost", 80
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    app.run()