from flask import Flask
from threading import Thread
from random import randint

app = Flask("")
@app.route("/")

def home():
  return("Online!")

def run():
  app.run(host = "0.0.0.0", port = randint(2000, 9000))

def keepAlive():
  thread = Thread(target = run)
  thread.start()