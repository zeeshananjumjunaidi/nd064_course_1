from flask import Flask,json
import logging


app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello Multiverse!"

@app.route('/metrics')
def metrics():
    app.logger.info('Metrics request successfull')
    return app.response_class(response=json.dumps({"data": {"UserCount": 140, "UserCountActive": 23}}),
    status=200,
    mimetype="application/json")


@app.route('/status')
def status():
    app.logger.info('Status request successfull')
    return app.response_class(response=json.dumps({"status":"success","result":"ok","code":0,}),
    status=200,
    mimetype="application/json")



if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
