from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /

def hello():                      # call method hello
    i=addition(1,2)
    j=division(3,4)
    k=division(10,4)
    return "Hello World! "+str(i)+" "+str(j)+" "+str(k)         # which returns "hello world"

def addition(a,b):
    return a+b

def division(a,b):
    if a>b:
        return a//b
    else:
        return b//a


if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app
