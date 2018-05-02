#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for, render_template, redirect
#from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path = "")
#auth = HTTPBasicAuth()

#@auth.get_password
#def get_password(username):
#    if username == 'maclain':
#        return 'python'
#    return None

#@auth.error_handler
#def unauthorized():
#    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
#    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

tasks = [
    {
        'id': 1,
        'command': u'scroll',
        'description': u'Welcome...',
    },
    {
        'id': 2,
        'command': u'scroll',
        'description': u'battery level ',
    }
]

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id = task['id'], _external = True)
        else:
            new_task[field] = task[field]
    return new_task

@app.route('/')
def home():

   return render_template('index_tasks.html', tasks=tasks)

@app.route('/sign/api/v1.0/tasks', methods = ['GET'])
#@auth.login_required
def get_tasks():
    return jsonify( { 'tasks': map(make_public_task, tasks) } )

@app.route('/sign/api/v1.0/tasks/<int:task_id>', methods = ['GET'])
#@auth.login_required
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify( { 'task': make_public_task(task[0]) } )

@app.route('/sign/api/v1.0/tasks', methods = ['POST'])
#@auth.login_required
def create_task():
    if not request.json or not 'command' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'command': request.json['command'],
        'description': request.json.get('description', ""),
    }
    tasks.append(task)
    return jsonify( { 'task': make_public_task(task) } ), 201

@app.route('/sign/api/v1.0/tasks/<int:task_id>', methods = ['PUT'])
#@auth.login_required
def update_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'command' in request.json and type(request.json['command']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    task[0]['command'] = request.json.get('command', task[0]['command'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    return jsonify( { 'task': (task[0]) } )

@app.route('/sign/api/v1.0/tasks/<int:task_id>', methods = ['DELETE'])
#@auth.login_required
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify( { 'result': True } )

if __name__ == '__main__':
    app.run(debug = True)
    #app.run(host= '0.0.0.0',port=5000, debug = True)
    
