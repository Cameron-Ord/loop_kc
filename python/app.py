#importing
import json
from flask import Flask
import dbhelper

app = Flask(__name__)

@app.get('/api/return_insert')
def select_dogs():
   #function that returns the results from run_proceedure when using respective arguments as JSON
   results = dbhelper.run_proceedure('CALL insert_item', [])
   if(type(results)==list):
    results_json = json.dumps(results, default=str)
   else:
      print('error')
   return results_json

#running @app
app.run(debug=True)
