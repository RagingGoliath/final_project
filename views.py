from flask import Flask
from flask.blueprints import Blueprint
from flask.templating import render_template
from flask import redirect, url_for
render_template

Views = Blueprint(__name__, "views")

@Views.route("/")

def homepage():
    return render_template("index.html")

@Views.route("/past")

def pastprojects():
    return render_template("pastprojects.html")

@Views.route("/present")

def currentproject():
    return render_template("currentproject.html")

@Views.route("/future")

def futureprojects():
    return render_template("futureprojects.html")

@Views.route("/about")

def about():
    return render_template("aboutcontact.html")

@Views.route("/home")

def home_redirect():
    return redirect(url_for("views.homepage"))

@Views.route("/Home")

def home_redirect2():
    return redirect(url_for("views.homepage"))

@Views.route("/HOME")

def home_redirect3():
    return redirect(url_for("views.homepage"))

@Views.route("/hOME")

def home_redirect4():
    return redirect(url_for("views.homepage"))

@Views.route("/main")

def main_redirect():
    return redirect(url_for("views.homepage"))

@Views.route("/Main")

def main_redirect2():
    return redirect(url_for("views.homepage"))

@Views.route("/mAIN")

def main_redirect3():
    return redirect(url_for("views.homepage"))

@Views.route("/MAIN")

def main_redirect4():
    return redirect(url_for("views.homepage"))

@Views.route("/dhg")

def dhg_redirect():
    return redirect(url_for("views.homepage"))

@Views.route("/Dhg")

def dhg_redirect2():
    return redirect(url_for("views.homepage"))

@Views.route("/DHG")

def dhg_redirect3():
    return redirect(url_for("views.homepage"))

@Views.route("/dHG")

def dhg_redirect4():
    return redirect(url_for("views.homepage"))

@Views.route("/Past")

def past_redirect():
    return redirect(url_for("views.pastprojects"))

@Views.route("/PAST")

def past_redirect2():
    return redirect(url_for("views.pastprojects"))

@Views.route("/pAST")

def past_redirect3():
    return redirect(url_for("views.pastprojects"))

@Views.route("/Present")

def present_redirect():
    return redirect(url_for("views.currentproject"))

@Views.route("/PRESENT")

def present_redirect2():
    return redirect(url_for("views.currentproject"))

@Views.route("/pRESENT")

def present_redirect3():
    return redirect(url_for("views.currentproject"))

@Views.route("/current")

def present_redirect4():
    return redirect(url_for("views.currentproject"))

@Views.route("/CURRENT")

def present_redirect5():
    return redirect(url_for("views.currentproject"))

@Views.route("/Current")

def present_redirect6():
    return redirect(url_for("views.currentproject"))

@Views.route("/cURRENT")

def present_redirect7():
    return redirect(url_for("views.currentproject"))

@Views.route("/Future")

def future_redirect():
    return redirect(url_for("views.futureprojects"))

@Views.route("/FUTURE")

def future_redirect2():
    return redirect(url_for("views.futureprojects"))

@Views.route("/fUTURE")

def future_redirect3():
    return redirect(url_for("views.futureprojects"))

@Views.route("/About")

def about_redirect():
    return redirect(url_for("views.about"))

@Views.route("/ABOUT")

def about_redirect2():
    return redirect(url_for("views.about"))

@Views.route("/aBOUT")

def about_redirect3():
    return redirect(url_for("views.about"))

@Views.route("/contact")

def about_redirect4():
    return redirect(url_for("views.about"))

@Views.route("/Contact")

def about_redirect5():
    return redirect(url_for("views.about"))

@Views.route("/CONTACT")

def about_redirect6():
    return redirect(url_for("views.about"))

@Views.route("/cONTACT")

def about_redirect7():
    return redirect(url_for("views.about"))