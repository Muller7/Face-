
from flask import Flask, request , json, render_template
from flask.ext.script import Manager
from flask_bootstrap import Bootstrap
from flask_cors import *
from b64 import b64decode
from face import facedis
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)
CORS(app, resources=r'/*')
#manager = Manager(app)

@app.route('/')
def hello():
    print 'Face Identification'
    stu_id = '1069833415090004'
    return render_template('index.html',stu_id=stu_id)

@app.route('/photo', methods=['POST','GET'])
def photo():

        
        data = json.loads(request.data)
       # print data['userNum']
       # stu_id = data['userNum']
        imgurl = data['image']  # operate the string 
        b64decode(imgurl) # create photo
        if ('userNum' in data):
            stu_id = data['userNum']
        else:
            stu_id = '1069833415090003'
        # compare
        try:
            
            dis = facedis(stu_id)
        except Exception:
            exception = json.dumps({'code':300,'str':'cannot find a face or no photos in file'})
            return exception
        else:
            print dis
            normal = json.dumps({'code':200,'str':dis})
            return normal

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True,port=5000,ssl_context='adhoc')
    #,ssl_context='adhoc'
