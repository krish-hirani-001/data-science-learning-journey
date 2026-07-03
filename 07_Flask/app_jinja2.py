from flask import Flask, render_template,redirect,url_for,request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "--welcome to our website--"

@app.route("/home")
def home():
    return render_template("home.html",name="krish",)

@app.route("/index",methods=["GET","POST"])
def home1():
    if request.method == "POST":
        name = request.form['name']
        return render_template("home.html",name=name)
    return render_template("form.html",name="name")

@app.route("/about",methods=["GET","POST"])
def home2():
    if request.method == "POST":
        age = int(request.form['age'])
        return render_template("abc.html",age=age)
    return render_template("form1.html",age="age")

@app.route("/about1")
def home3():
    students=['krish','yash','meet','ayush','jenish']
    return render_template("xyz.html",students=students)

if __name__ == "__main__":
    app.run(debug=True)