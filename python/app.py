#importing
import json
from flask import Flask, request
import dbhelper
import api_helper

app = Flask(__name__)


@app.post('/api/return_insert')
def return_insert():
   error=api_helper.check_endpoint_info(request.json, ['username', 'password', 'is_prenium'])
   if(error != None):
      return 'something went wrong'
   results = dbhelper.run_proceedure('CALL return_insert(?,?,?)', [request.json.get('username'), request.json.get('password'), request.json.get('is_prenium')])
   return json.dumps(results, default=str)

#running @app

@app.patch('/api/update_client')
def update_client():
   error=api_helper.check_endpoint_info(request.json, ['username', 'password', 'new_password'])
   if(error != None):
      return 'something went wrong'
   results = dbhelper.run_proceedure('CALL update_pass(?,?,?)', [request.json.get('username'), request.json.get('password'), request.json.get('new_password')])
   return json.dumps(results, default=str)
app.run(debug=True)