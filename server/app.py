from flask import Flask, Response, jsonify, send_file
import pandas as pd
import os

app = Flask(__name__)

@app.route("/")
def app_root():
    return "Welcome!"

@app.route("/api/ron")
def serve_ron():
    return send_file('./imgs/ron.gif', mimetype='image/gif')

@app.route("/api/boythrow")
def serve_boythrow():
    return send_file('./imgs/boythrow.gif', mimetype='image/gif')

@app.route("/api/team")
def get_team_members():
    # df = pd.read_csv('.\\data\\team.csv', header=0)
    # return df.to_json(orient='split')
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    tst_dir = os.path.split(__file__)
    csv_path = os.path.join(cur_dir, '\\data\\team.csv')
    return tst_dir

@app.route("/api/legit")
def api_legit():
    data = [
        {
        'name' : 'Bob',
        'age' : 23
        },{
        'name' : 'Sally',
        'age' : 31
        }
    ]
    resp = jsonify(data)
    resp.status_code = 200
    return resp 

@app.route("/api/morelegit")
def app_morelegit():
    data = [
        {
        'img' : 'dilbert',
        'url' : '/api/boythrow',
        'title' : 'Not testing code before delivery'
        },{
        'img' : 'ron.gif',
        'url' : '/api/ron',
        'title' : 'Time to go learn...'
        }
    ]
    resp = jsonify(data)
    resp.status_code = 200
    return resp 

if __name__ == '__main__':
    app.run(port=5050,debug=True)