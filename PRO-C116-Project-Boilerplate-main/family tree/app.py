# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument


# write the routes using decorator functions
# default route or 'URL'
app = Flask(__name__)
@app.route("/")
def home():

    name = "Yajat" # write your name
    age = "12" # write your age

    return render_template("index.html" , name = name , age = age)

# define the route to father webpage
@app.route("/Father")
def father():

    name = "Shree" 
    age = "38"  

    return render_template("father.html" , name = name , age = age)

# define the route to mother webpage
@app.route("/Mother")
def mother():

    name = "Premlata" 
    age = "34"

    return render_template("mother.html" , name = name , age = age)

# define the route to friends webpage

@app.route("/Friend")
def friend():

    name = "Krithik" 
    age = "12"

    return render_template("friend.html" , name = name , age = age)


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
