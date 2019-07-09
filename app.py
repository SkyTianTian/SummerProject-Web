from flask import Flask
import os
import AIR

app = Flask(__name__, static_url_path='')
#app = Flask(__name__)
port = int(os.getenv('PORT', 8000))


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')
    #print("Hello World")
    #return "Hello New World 2.0"

@app.route("/test",methods=['POST','GET'])
def test():
    return AIR.test()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)
