from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route("/")
def wel():
    return "welcome to home page"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about",methods=['GET'])
def about():
    name=request.args.get("name")
    return f"welcome to {name}"

@app.route("/form", methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        name = request.form['name']
        return f"Welcome {name}"
    return render_template("form.html", name="name")

@app.route("/form1",methods=['GET','POST'])
def welcome1():
    if request.method == 'POST':
        name=request.form['name']
        return render_template("index.html",name=name)
    return render_template("form.html",name="name")

@app.route("/form2",methods=['GET','POST'])
def welcome2():
    if request.method == 'POST':
        name=request.form['name']
        return redirect(url_for("about",name=name))
    return render_template("form.html",name="name")

if __name__ == '__main__':
    app.run(debug=True)