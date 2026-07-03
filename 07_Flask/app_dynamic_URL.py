from flask import Flask,render_template,redirect,request,url_for

app = Flask(__name__)

@app.route("/")
def wel():
    return f"welcome coders"

@app.route("/home/<name>")
def user(name):
    return f"hello {name}"

@app.route("/index/<int:age>")
def abc(age):
    if age>=18:
        return f"you are Eligible.yor age is {age}"
    else :
        return f"you are not Eligible.Because you age is {age}"

@app.route("/about",methods=["GET","POST"])
def home2():
    if request.method == "POST":
        age = int(request.form['age'])
        return redirect(url_for("abc",age=age))
    return render_template("form1.html",age="age")

@app.route("/price/<float:amt>")
def price(amt):
    return f"price : {amt}"

@app.route("/stud/<name>/<int:roll>")
def stud(name,roll):
    return f"Name : {name} Rollno : {roll}"


if __name__ == '__main__':
    app.run(debug=True) 