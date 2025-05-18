from flask import Flask, render_template, request, redirect
from display import menus


app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


@app.route("/", methods=["get", "post"])
def welcome():
    return render_template(
        "home.html",
        dashboard=menus.dashboard_menus,
        company_list_all=menus.company_list_all,
    )


@app.route("/createcompany", methods=["get", "post"])
def create_company():
    return render_template(
        "create_company.html",
        dashboard=menus.dashboard_menus,
    )


@app.route("/companybalance", methods=["get", "post"])
def company_balance():
    return render_template(
        "company_balance.html",
        dashboard=menus.dashboard_menus,
        company_list_transaction_list=menus.company_list_transaction,
    )


@app.route("/editcompany", methods=["get", "post"])
def edit_company():
    return render_template(
        "edit_company.html",
        dashboard=menus.dashboard_menus,
    )


@app.route("/privileges", methods=["get", "post"])
def privileges():
    return render_template(
        "privileges.html",
        dashboard=menus.dashboard_menus,
    )


@app.route("/settings", methods=["get", "post"])
def settings():
    return render_template(
        "settings.html",
        dashboard=menus.dashboard_menus,
    )


@app.route("/blacklist", methods=["get", "post"])
def blacklisted():
    return render_template(
        "blacklisted.html",
        dashboard=menus.dashboard_menus,
    )


if __name__ == "__main__":
    app.run("localhost", 5000, debug=True)
