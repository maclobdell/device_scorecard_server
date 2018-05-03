#!flask/bin/python
from __future__ import print_function

from flask import Flask, jsonify, abort, request, make_response, url_for, render_template, redirect
#from flask.ext.httpauth import HTTPBasicAuth

import sys

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
        'name': 'LPC546XX',
        'description': [
            {
                "ver": "Mbed OS 5.8",
                "name": "LPC546XX",
                "date": "May 2, 2018",
                "target_data" : { 'FLASH': 'N', 'RTC': 'Y', 'SPI': 'Y', 'I2C': 'Y', 'TRNG': 'N', 'SLEEP': 'Y'}
            },            
            {
                "ver": "Mbed OS 5.7",
                "name": "LPC546XX",
                "date": "May 2, 2018",
                "target_data" : { 'FLASH': 'N', 'RTC': 'N', 'SPI': 'N', 'I2C': 'Y', 'TRNG': 'N', 'SLEEP': 'Y'}
            }  
        ],                     
        'uri' : 'x'
    },
    {
        'id': 2,
        'name': 'LPC54114',
        'description': [
            {
                "ver": "Mbed OS 5.8",
                "name": "LPC54114",
                "date": "May 2, 2018",
                "target_data" : { 'FLASH': 'N', 'RTC': 'Y', 'SPI': 'N', 'I2C': 'Y', 'TRNG': 'N', 'SLEEP': 'Y'}
            },            
            {
                "ver": "Mbed OS 5.7",
                "name": "LPC54114",
                "date": "May 2, 2018",
                "target_data" : { 'FLASH': 'Y', 'RTC': 'Y', 'SPI': 'N', 'I2C': 'Y', 'TRNG': 'N', 'SLEEP': 'Y'}
            }  
        ],                     
        'uri' : 'x'
    },
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
    return render_template('scorecard_template.html', target_data=target[0])
   
   

@app.route('/target_data/api/v1.0/targets', methods = ['GET'])
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
    print(" update_target", file=sys.stderr)
     
    if len(target) == 0:
        print (" length of target zero", file=sys.stderr)
        abort(404)
    if not request.json:
       print(" not proper json", file=sys.stderr)
       abort(400) 
              
    print(request.json, file=sys.stderr)
    #print(request.json, file=sys.stderr)
         
    #.get('description'), file=sys.stderr)
    #target[0]['description'].append(request.json.get('description', target[0]['description']))
    target[0]['description'] = (request.json.get('description')) + target[0]['description']
        
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
    
