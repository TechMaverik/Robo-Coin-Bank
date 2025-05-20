import sqlite3
import random
from queries.querysets import *


class Mappers:

    def add_company_details(self, model):
        id = random.randint(1, 1000000)
        with sqlite3.connect("database/robocoin.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                INSERT_COMPANY_DETAILS,
                (
                    model.company,
                    model.ceo,
                    model.grade,
                    model.division,
                    model.s1,
                    model.s2,
                    model.s3,
                    model.s4,
                    model.s5,
                    model.s6,
                    model.balance,
                    model.strike,
                    model.remarks,
                    id,
                ),
            )
            connection.commit()
        connection.close()
        return True

    def load_all_company_details(self):
        with sqlite3.connect("database/robocoin.db") as connection:
            cursor = connection.cursor()
            cursor.execute(SELECT_ALL_COMPANY_DETAILS)
            rows = cursor.fetchall()
        connection.close()
        return rows

    def sort_students_with_grade(self, model):
        with sqlite3.connect("database/robocoin.db") as connection:
            cursor = connection.cursor()
            cursor.execute(SORT_STUDNETS, (model.grade, model.division))
            rows = cursor.fetchall()
        connection.close()
        return rows

    def load_company_with_ceo(self, model):
        with sqlite3.connect("database/robocoin.db") as connection:
            cursor = connection.cursor()
            cursor.execute(SELECT_ALL_WITH_CEO, (model.ceo,))
            rows = cursor.fetchall()
        connection.close()
        return rows

    def update_robocoin(self, model):
        balance = 0
        with sqlite3.connect("database/robocoin.db") as connection:
            cursor = connection.cursor()
            cursor.execute(GET_BALANCE, (model.id,))
            coins_to_add = model.balance
            rows = cursor.fetchone()
            balance = rows[0] + int(coins_to_add)
        connection.close()
        with sqlite3.connect("database/robocoin.db") as connection:
            print(balance)
            cursor = connection.cursor()
            cursor.execute(
                UPDATE_COIN,
                (
                    balance,
                    model.id,
                ),
            )
        connection.commit()
        connection.close()

        print(balance)
        return True

    def update_strikes(self, model):
        strikes = 0

        with sqlite3.connect("database/robocoin.db") as connection:
            cursor = connection.cursor()
            cursor.execute(GET_STRIKES, (model.id,))
            rows = cursor.fetchone()
            strikes = rows[0] + 1
        connection.close()
        with sqlite3.connect("database/robocoin.db") as connection:
            remarks = model.remarks
            cursor = connection.cursor()
            cursor.execute(
                UPDATE_STRIKES,
                (
                    strikes,
                    remarks,
                    model.id,
                ),
            )
        connection.commit()
        connection.close()
        print(strikes)
        return True

    def load_blacklisted_company_details(self):
        with sqlite3.connect("database/robocoin.db") as connection:
            cursor = connection.cursor()
            cursor.execute(SELECT_BLACK_COMPANY_DETAILS, (1,))
            rows = cursor.fetchall()
        connection.close()
        return rows
