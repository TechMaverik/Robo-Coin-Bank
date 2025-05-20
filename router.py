from flask import Flask, render_template, request, redirect
from display import menus
from services import Services

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


@app.route("/", methods=["get", "post"])
def welcome():
    rows = Services().load_all_company_details()
    return render_template(
        "home.html",
        dashboard=menus.dashboard_menus,
        company_list_all=menus.company_list_all,
        company_details=rows,
    )


@app.route("/sort", methods=["get", "post"])
def sort():
    rows = Services().sort_students_with_grade()
    return render_template(
        "home.html",
        dashboard=menus.dashboard_menus,
        company_list_all=menus.company_list_all,
        company_details=rows,
    )


@app.route("/createcompany", methods=["get", "post"])
def create_company():

    return render_template(
        "create_company.html",
        dashboard=menus.dashboard_menus,
    )


@app.route("/load_company", methods=["get", "post"])
def load_company():
    status = Services().add_company_details()
    return render_template(
        "create_company.html",
        dashboard=menus.dashboard_menus,
        status=status,
    )


@app.route("/transactions", methods=["get", "post"])
def company_balance():
    return render_template(
        "transactions.html",
        dashboard=menus.dashboard_menus,
        company_list_transaction_list=menus.company_list_transaction,
    )


@app.route("/searchceo", methods=["get", "post"])
def search_ceo():
    rows = Services().load_company_details_with_ceo()
    return render_template(
        "transactions.html",
        dashboard=menus.dashboard_menus,
        company_list_transaction_list=menus.company_list_transaction,
        rows=rows,
    )


@app.route("/updatebalance", methods=["get", "post"])
def update_robocoins():
    Services().update_robocoins()
    return render_template(
        "transactions.html",
        dashboard=menus.dashboard_menus,
        company_list_transaction_list=menus.company_list_transaction,
    )


@app.route("/updatestrikes", methods=["get", "post"])
def update_strikes():
    Services().update_strikes()
    return render_template(
        "transactions.html",
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
    rows = Services().load_blacklisted()
    return render_template(
        "blacklisted.html",
        dashboard=menus.dashboard_menus,
        black_listed_companies=menus.black_listed_companies_table,
        blacklisted=rows,
    )


if __name__ == "__main__":
    app.run("10.120.3.167", 5000, debug=True)
