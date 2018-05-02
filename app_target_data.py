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

targets = [
    {
        'id': 1,
        'name': u'target1',
        'description': 
            { 'FLASH': 'x', 'RTC': 'x', 'SPI': 'x', 'I2C': 'x', 'TRNG': 'x', 'SLEEP': 'x'},
        'uri' : 'x'
    },
    {
        'id': 2,
        'name': u'target2',
        'description': 
            { 'FLASH': 'x', 'RTC': 'x', 'SPI': 'x', 'I2C': 'x', 'TRNG': 'x', 'SLEEP': 'x'},
        'uri' : 'x'
    }
]

def make_public_target(target):
    new_target = {}
    for field in target:
        if field == 'id':
            new_target['uri'] = url_for('get_target', target_id = target['id'], _external = True)
        else:
            new_target[field] = target[field]
    return new_target

@app.route('/')
def home():

   for target in targets:
       for field in target:
           if field == 'id':
               target['uri'] = url_for('show_target', target_id = target['id'], _external = True)
               
   return render_template('index_targets.html', targets=targets)


@app.route('/target_data/<int:target_id>')
def show_target(target_id):

    target = filter(lambda t: t['id'] == target_id, targets)
    if len(target) == 0:
        abort(404)
    return render_template('target_data.html', target_data=target[0])
   
   

@app.route('/target_data/api/v1.0/target', methods = ['GET'])
#@auth.login_required
def get_targets():
    return jsonify( { 'targets': map(make_public_target, targets) } )

@app.route('/target_data/api/v1.0/targets/<int:target_id>', methods = ['GET'])
#@auth.login_required
def get_target(target_id):
    target = filter(lambda t: t['id'] == target_id, targets)
    if len(target) == 0:
        abort(404)
    return jsonify( { 'target': make_public_target(target[0]) } )

@app.route('/target_data/api/v1.0/targets', methods = ['POST'])
#@auth.login_required
def create_target():
    if not request.json or not 'name' in request.json:
        abort(400)
    target = {
        'id': targets[-1]['id'] + 1,
        'name': request.json['name'],
        'description': request.json.get('description', ""),
    }
    targets.append(target)
    return jsonify( { 'target': make_public_target(target) } ), 201

@app.route('/target_data/api/v1.0/targets/<int:target_id>', methods = ['PUT'])
#@auth.login_required
def update_target(target_id):
    target = filter(lambda t: t['id'] == target_id, targets)
    if len(target) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    target[0]['name'] = request.json.get('name', target[0]['name'])
    target[0]['description'] = request.json.get('description', target[0]['description'])
    return jsonify( { 'target': (target[0]) } )

@app.route('/target_data/api/v1.0/targets/<int:target_id>', methods = ['DELETE'])
#@auth.login_required
def delete_target(target_id):
    target = filter(lambda t: t['id'] == target_id, targets)
    if len(target) == 0:
        abort(404)
    targets.remove(target[0])
    return jsonify( { 'result': True } )

if __name__ == '__main__':
    app.run(debug = True)
    #app.run(host= '0.0.0.0',port=5000, debug = True)
    
