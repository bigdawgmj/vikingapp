from flask import Flask, Response, jsonify, send_file, request
import pandas as pd
import os
import pdb
from vsts import VstsWorker
from configparser import ConfigParser

app = Flask(__name__)

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
    # pdb.set_trace()
    content = request.get_json()
    csv_str = '\r' + content['id'] + ',' + content['firstname'] + ',' + content['lastname'] + ',' + content['email']

    csv_path = os.path.join(os.getcwd(), 'server\\data\\team.csv')
    csv_file = open(csv_path, 'a')
    csv_file.write(csv_str)
    csv_file.close()

    return jsonify({"status": "SUCCESS"})

@app.route('/api/wit/training', methods=['POST'])
def add_training():
    content = request.get_json()
    sprint = content['sprint']
    weeks = ['wk1', 'wk2']
    config = ConfigParser() 
    ini_path = os.path.join(os.getcwd(), 'server\\vsts_config.ini')
    config.read(ini_path)
    # pdb.set_trace()

    vsts = VstsWorker(
        config.get('vsts', 'base_url'),
        config.get('vsts', 'username'),
        config.get('vsts', 'pat'),
        config.get('vsts', 'project')
    )

    csv_path = os.path.join(os.getcwd(), 'server\\data\\team.csv')
    df = pd.read_csv(csv_path, header=0)
    team = df.to_dict(orient='records')

    wit_url = vsts.base_url + 'DefaultCollection/_apis/wit/$batch?api-version=2.0'
    data = vsts.create_training_data(sprint, team, weeks)
    result = vsts.create_request(wit_url, data)
    
    print result.getcode()
    return jsonify({'status': 'SUCCESS'})

# @app.route("/")
# def app_root():
#     return "Welcome!"

# @app.route("/api/ron")
# def serve_ron():
#     return send_file('./imgs/ron.gif', mimetype='image/gif')

# @app.route("/api/boythrow")
# def serve_boythrow():
#     return send_file('./imgs/boythrow.gif', mimetype='image/gif')

# @app.route("/api/legit")
# def api_legit():
#     data = [
#         {
#         'name' : 'Bob',
#         'age' : 23
#         },{
#         'name' : 'Sally',
#         'age' : 31
#         }
#     ]
#     resp = jsonify(data)
#     resp.status_code = 200
#     return resp 

# @app.route("/api/morelegit")
# def app_morelegit():
#     data = [
#         {
#         'img' : 'dilbert',
#         'url' : '/api/boythrow',
#         'title' : 'Not testing code before delivery'
#         },{
#         'img' : 'ron.gif',
#         'url' : '/api/ron',
#         'title' : 'Time to go learn...'
#         }
#     ]
#     resp = jsonify(data)
#     resp.status_code = 200
#     return resp 


if __name__ == '__main__':
    app.run(port=5050,debug=True)