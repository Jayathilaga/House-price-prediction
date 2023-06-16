from flask import Flask,jsonify,request,make_response
import time
from collections import OrderedDict
app = Flask(__name__)
@app.errorhandler(404)
def resource_not_found(e):
    return "(404)"

@app.route('/timestamp')
def hello_world():
    current_timestamp = int(time.time())
    return jsonify({'timestamp': current_timestamp})

@app.route('/readdata', methods=['POST'])
def handle_json():
    
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        response ={
            'username':json.get('username'),
            'password':json.get('password')
                    }

        return make_response(jsonify(response))
    else:
        return 'Content-Type not supported!'
#     if ( request.is_json):
#         req=request.get_json()
#         response ={
#             'username':req.get('username'),
#             'password':req.get('password')
        
#                     }
#     return jsonify(response)

if __name__ == '__main__':
    app.run(host='127.0.0.1')