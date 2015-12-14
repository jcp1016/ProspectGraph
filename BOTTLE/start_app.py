import json, os
from bottle import get, post, route, run, debug, request, response, static_file, template
import json
#from py2neo import GraphDatabaseService, CypherQuery

#run(reloader = True)

# set connection information (defaults to http://localhost:7474/db/data/)
#graph_db = GraphDatabaseService()

@route('/js/<filename>')
def js_static(filename):
    return static_file(filename, root='./js')

@route('/img/<filename>')
def img_static(filename):
    return static_file(filename, root='./img')

@route('/css/<filename>')
def img_static(filename):
    return static_file(filename, root='./css')

@route('/')
def index():
    return template("index.tpl", url='')

@route('/', method='POST')
def submit(url=''):
    orgname = request.forms.get('orgname').strip().lower()
    if orgname:
        orgurl = "http://www." + orgname + ".org"
        #raw_items = os.system("python site_keywords.py " + orgurl + " 20")
    else:
        orgurl = "Error: please enter an organization name."
    return template("index.tpl", url=orgurl)

if os.system('whoami') == 'Columbia':
    run(host='10.0.0.8', port=8080, debug=False)
else:
    run(host='localhost', port=8080, debug=False)

