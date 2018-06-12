import urllib2, base64, json, configparser
import pandas as pd
import pdb
import math

class VstsWorker:
    def __init__(self, base_url, username, pat, project=None):
        self.base_url = str(base_url) 
        self.username = str(username)
        self.pat = str(pat)
        self.project = str(project)

    def create_request(self, url, data=None):
        # pdb.set_trace()
        if data is None:
            self.request = urllib2.Request(url)
        else:
            self.request = urllib2.Request(url, data, {'Content-Type': 'application/json'})

        base64_str = base64.encodestring('%s:%s' % (self.username, self.pat)).replace('\n', '')
        self.request.add_header("Authorization", "Basic %s" % base64_str)
        result = urllib2.urlopen(self.request)
        return result

    def create_wit(self, project, wit_name):
        wit_url = self.base_url + 'DefaultCollection/' + project + '/_apis/wit/workitems/$' + wit_name + '?api-version=2.0'
        json_obj = json.load(self.create_request(wit_url))

    def create_training_data(self, sprint, users, weeks):
        tasks = []

        # pdb.set_trace()
        pbi = {}
        pbi['method'] = 'PATCH'
        pbi['uri'] = '/' + self.project + '/_apis/wit/workItems/$Product Backlog Item?api-version=2.0'
        pbi['headers'] = {'Content-Type' : 'application/json-patch+json'}
        pbi['body'] = [ { 
            'op' : 'add',  
            'path' : '/fields/System.Title',  
            'value' : 'Sprint ' + str(sprint) + ' Training'  
        }, {
            'op' : 'add',  
            'path' : '/fields/System.IterationPath',  
            'value' : self.project + '\\Sprint ' + str(sprint)  
        }, {
            'op' : 'add',  
            'path' : '/fields/Microsoft.VSTS.Scheduling.Effort',  
            'value' : len(users) * 2
        }, {
            'op': 'add',
            'path' : '/id',
            'value' : '-1'
        } ]
        tasks.append(pbi)

        cnt = 1
        for user in users:
            # firstname = user['name'].split(' ')[0]
            # pdb.set_trace()
            name = user['firstname'] + ' ' + user['lastname']
            for week in weeks:
                cnt += 1
                training = {}
                training['method'] = 'PATCH'
                training['uri'] = '/' + self.project + '/_apis/wit/workItems/$Task?api-version=2.0'
                training['headers'] = {'Content-Type' : 'application/json-patch+json'}
                training['body'] = [ { 
                    'op' : 'add',  
                    'path' : '/fields/System.Title',  
                    'value' : user['firstname'] + ' ' + week + ' training'  
                }, {
                    'op' : 'add',  
                    'path' : '/fields/System.IterationPath',  
                    'value' : self.project + '\\Sprint ' + str(sprint)  
                }, {
                    'op' : 'add',  
                    'path' : '/fields/System.AssignedTo',  
                    'value' : name # + ' ' +  user['email']   
                }, {
                    'op' : 'add',  
                    'path' : '/fields/Microsoft.VSTS.Scheduling.RemainingWork',  
                    'value' : 1.0  
                }, {
                    'op': 'add',
                    'path' : '/id',
                    'value' : '-' + str(cnt)
                }, {
                    'op': 'add',
                    'path': '/relations/-',
                    'value': {
                        'rel': 'System.LinkTypes.Hierarchy-Reverse',
                        'url': self.base_url + 'DefaultCollection/' + self.project + '/_apis/wit/workItems/-1'
                        }
                } ]
                tasks.append(training)

        data = json.dumps(tasks)
        return data

    def get_iterations(self):
        url = self.base_url + 'DefaultCollection/' + self.project + '/_apis/wit/classificationNodes/iterations?$depth=2&api-version=2.0'
        result = self.create_request(url) 
        data = json.load(result)