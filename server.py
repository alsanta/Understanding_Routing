from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def success():
    return "Dojo"

@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hello, " + str(name)

@app.route('/repeat/<number>/<word>')
def repeat(number,word):
    stuff = ''
    for x in range(0,int(number)):
        stuff += f'{word}\n'
    return stuff

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."

# Ensure this file is being run directly and not from a different module
# Run the app in debug mode.
if __name__=="__main__":
    app.run(debug=True)