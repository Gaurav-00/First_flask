from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")     #here we specify route /
def welcome():
    return "<h1>Hello</h1>"
@app.route("/contact")
def contact_page():
    return render_template("contact.html")
@app.route("/home")
def home_page():
    return "Home page"
@app.route("/gallery")
def gallery_page():
    return "Gallery page"
if __name__=="__main__":
    app.run()

