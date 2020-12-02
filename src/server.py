from flask import Flask, request
from scrap import price

server = Flask(__name__)

@server.route("/price")
def hello():
    return price(request.args.get('product'))

if __name__ == "__main__":
   server.run(host='0.0.0.0')