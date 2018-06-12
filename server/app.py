from flask import Flask, Response, jsonify, send_file, request
import pandas as pd
import os
import pdb
from vsts import VstsWorker
from configparser import ConfigParser
import json
from WeatherUndergroundAccess import WeatherUndergroundAccess as WU

app = Flask(__name__)

@app.route("/api/team")
def get_team_members():
    # cur_dir = os.path.dirname(os.path.realpath(__file__))
    # tst_dir = os.path.split(__file__)
    csv_path = os.path.join(os.getcwd(), 'server\\data\\team.csv')
    df = pd.read_csv(csv_path, header=0)
    return df.to_json(orient='records')
    # return csv_path 

@app.route("/api/weather/<city>")
def get_weather(city):
    return WU().get_weather(city)

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

@app.route('/api/projects', methods=['GET'])
def get_projects():
    config = ConfigParser() 
    ini_path = os.path.join(os.getcwd(), 'server\\vsts_config.ini')
    config.read(ini_path)
    vsts = VstsWorker(
        config.get('vsts', 'base_url'),
        config.get('vsts', 'username'),
        config.get('vsts', 'pat')
    )

    result = vsts.create_request(vsts.base_url + '/DefaultCollection/_apis/projects?api-version=2.0')
    data = json.load(result)
    values = data['value']
    out_array = []
    for val in values:
        output = {'id':val['id'],'name':val['name']}
        out_array.append(output)
    # return jsonify(result) 
    return jsonify(out_array)

@app.route('/api/wit/training', methods=['POST'])
def add_training():
    content = request.get_json()
    sprint = content['sprint']
    project = content['project']
    weeks = ['wk1', 'wk2']
    config = ConfigParser() 
    ini_path = os.path.join(os.getcwd(), 'server\\vsts_config.ini')
    config.read(ini_path)

    vsts = VstsWorker(
        config.get('vsts', 'base_url'),
        config.get('vsts', 'username'),
        config.get('vsts', 'pat'),
        project
    )

    # TODO: Need to update team to have vsts name
    csv_path = os.path.join(os.getcwd(), 'server\\data\\team.csv')
    df = pd.read_csv(csv_path)
    df = df.fillna('')
    team = df.to_dict(orient='records')

    wit_url = vsts.base_url + 'DefaultCollection/_apis/wit/$batch?api-version=2.0'
    data = vsts.create_training_data(sprint, team, weeks)
    result = vsts.create_request(wit_url, data)
    
    print result.getcode()
    return jsonify({'status': 'SUCCESS'})


if __name__ == '__main__':
    app.run(port=5050,debug=True)