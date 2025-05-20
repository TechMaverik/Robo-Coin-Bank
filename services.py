from flask import request
from models.company import AddCompany
from mappers import Mappers


class Services:

    def add_company_details(self):
        if request.method == "POST":
            self.company_details = AddCompany(
                company=request.form["name"],
                ceo=request.form["ceo"],
                grade=request.form["grade"],
                division=request.form["division"],
                s1=request.form["s1"],
                s2=request.form["s2"],
                s3=request.form["s3"],
                s4=request.form["s4"],
                s5=request.form["s5"],
                s6=request.form["s6"],
                balance=request.form["balance"],
                strike=request.form["strikes"],
                remarks=request.form["remarks"],
            )
        status = Mappers().add_company_details(self.company_details)
        return status

    def load_all_company_details(self):
        if request.method == "GET":
            rows = Mappers().load_all_company_details()
            return rows

    def sort_students_with_grade(self):
        if request.method == "POST":
            self.company_details = AddCompany(
                grade=request.form["grade"],
                division=request.form["division"],
            )
            rows = Mappers().sort_students_with_grade(self.company_details)
            return rows

    def load_company_details_with_ceo(self):
        if request.method == "POST":
            self.company_details = AddCompany(
                ceo=request.form["name"],
            )
            rows = Mappers().load_company_with_ceo(self.company_details)
            return rows

    def update_robocoins(self):
        if request.method == "POST":
            self.company_details = AddCompany(
                id=request.form["id"],
                balance=request.form["coins"],
            )
            status = Mappers().update_robocoin(self.company_details)
            return status

    def update_strikes(self):
        if request.method == "POST":
            self.company_details = AddCompany(
                id=request.form["id"],
                remarks=request.form["remarks"],
            )
            status = Mappers().update_strikes(self.company_details)
            return status

    def load_blacklisted(self):
        rows = Mappers().load_blacklisted_company_details()
        return rows
