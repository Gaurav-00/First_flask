from flask import Flask
app=Flask(__name__)

@app.route("/")     #here we specify route /
def welcome():
    return "Welcome to my website"
@app.route("/contact")
def contact_page():
    return "Contact page"
@app.route("/home")
def home_page():
    return "Home page"
@app.route("/gallery")
def gallery_page():
    return "Gallery page"
if __name__=="__main__":
    app.run()

