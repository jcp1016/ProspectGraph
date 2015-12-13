import json, os
from bottle import route, run, request, response, static_file, template, view
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
    return static_file("index.html", root=".")
    #return '''
    #    <form action="/get_url", method="post">
    #        orgname: <input name="orgname" type="text" />
    #    </form>
    #'''

@route('/get_url', method='POST')
def get_url():
    orgname = request.forms.get('orgname').strip().lower()
    if orgname:
        orgurl = "<p>http://www." + orgname + ".org</p>"
        return orgurl
    else:
        return "<p>Error: please enter an organizatin name.</p>" 
                         
                          
@route("/search")
def do_search():
    return

run(host='localhost', port=8080, debug=False)
