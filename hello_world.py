from flask import Flask, render_template
#get access to environment variables from Cloud9
from os import environ

#Create instance of the Flask class called "app"
#pass in the __name__ variable to tell the app where it is being run from
app = Flask(__name__)

#Used for every Flask view. 
#Means that when you visit either the root URL or 
#the /hello URL the function should run
@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
    
@app.route("/hello/<name>")
#def hi_person(name):
#    return "Hello {}!".format(name.title())

#Return HTML example
def hello_person(name):
    return render_template('template.html', my_string="Hello {}!".format(name.title()))
    
    #html = """
    #    <h1>
    #        Hello {}!
    #    </h1>
    #    <p>
    #        Here's a picture of a kitten.  Awww...
    #    </p>
    #    <img src="http://placekitten.com/g/200/300">
    #"""
    #return html.format(name.title())

@app.route("/jedi/<first>/<last>")
def hi_jedi(first,last):
    return "Your Jedi name is {}{}!".format(last[0:3], first[0:2])

#Run app
#host and port argument tell app to listen on the
#values from workspace environment
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
            