from flask import Flask, Response, jsonify, send_file, request
import pandas as pd
import os
import pdb

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
    # cur_dir = os.path.dirname(os.path.realpath(__file__))
    # tst_dir = os.path.split(__file__)
    csv_path = os.path.join(os.getcwd(), 'server\\data\\team.csv')
    df = pd.read_csv(csv_path, header=0)
    return df.to_json(orient='records')
    # return csv_path 

@app.route('/api/team/member', methods=['POST'])
def post_team_member():
    pdb.set_trace()
    content = request.get_json()
    csv_str = '\r' + content['id'] + ',' + content['firstname'] + ',' + content['lastname'] + ',' + content['email']

    csv_path = os.path.join(os.getcwd(), 'server\\data\\team.csv')
    csv_file = open(csv_path, 'a')
    csv_file.write(csv_str)
    csv_file.close()

    return jsonify({"status": "SUCCESS"})

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