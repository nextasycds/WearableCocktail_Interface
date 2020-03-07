from flask import Flask 


#referencing the file
app = Flask(__name__) 

#set up route so we don't automatically end up at 404
@app.route('/')
def index(): 
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True)

