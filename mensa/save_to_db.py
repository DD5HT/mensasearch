# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
import sqlite3
from items import MealEntry

def date_generator(date_string):
    date_fields = date_string.split(" ")
    date = date_fields[3]
    date += "-"
    month = date_fields[2]
    if month == u"Januar":
        date += "01"
    elif month == u"Februar":
        date += "02"
    elif month == u"März":
        date += "03"
    elif month == u"April":
        date += "04"
    elif month == u"Mai":
        date += "05"
    elif month == u"Juni":
        date += "06"
    elif month == u"Juli":
        date += "07"
    elif month == u"August":
        date += "08"
    elif month == u"September":
        date += "09"
    elif month == u"October":
        date += "10"
    elif month == u"November":
        date += "11"
    elif month == u"Dezember":
        date += "12"
    date += "-" + date_fields[1].replace('.', '')
    return date

def meal_lable_generator(meal, lables):
    out = []
    for f in lables:
        out.append((meal, f))
    return out

def lable_insert(sqlcursor, meal, lables):
    for l in lables:
        sqlcursor.execute("INSERT OR IGNORE INTO lable (name) VALUES (?)", (l, ))
    sqlcursor.executemany("INSERT OR IGNORE INTO meal_has_lable (meal,lable) VALUES (?,?)", meal_lable_generator(meal, lables))

class MensaPipeline(object):

    def __init__(self):
        self.conn = sqlite3.connect("./mensa.sqlite")
        self.c = self.conn.cursor()
        self.c.executescript("""
        CREATE TABLE IF NOT EXISTS kind (
            name TEXT NOT NULL PRIMARY KEY
        );
        CREATE TABLE IF NOT EXISTS meal (
            description TEXT NOT NULL PRIMARY KEY,
            kind TEXT NOT NULL,
            FOREIGN KEY (kind) REFERENCES kind(name)
        );
        CREATE TABLE IF NOT EXISTS mensa (
            name TEXT NOT NULL PRIMARY KEY,
            location_lo REAL DEFAULT 0.0,
            location_la REAL DEFAULT 0.0
        );
        CREATE TABLE IF NOT EXISTS lable (
            name TEXT NOT NULL PRIMARY KEY,
            description TEXT
        );
        CREATE TABLE IF NOT EXISTS meal_has_lable (
            meal description NOT NULL,
            lable INTEGER NOT NULL,
            since TEXT DEFAULT CURRENT_TIME,
            FOREIGN KEY (meal) REFERENCES meal(description),
            FOREIGN KEY (lable) REFERENCES lable(name),
            PRIMARY KEY (meal, lable)
        );
        CREATE TABLE IF NOT EXISTS mensa_has_meal (
            meal TEXT NOT NULL,
            mensa INTEGER NOT NULL,
            avail_date TEXT DEFAULT CURRENT_DATE,
            avail_time DEFAULT "Mittagsmensa",
            price_student INTEGER NOT NULL,
            price_employee INTEGER NOT NULL,
            price_guest INTEGER NOT NULL,
            FOREIGN KEY (meal) REFERENCES meal(description),
            FOREIGN KEY (mensa) REFERENCES mensa(name),
            PRIMARY KEY (mensa, meal, avail_date, avail_time)
         );
         """)

    def spider_closed(self,spider,reason):
        self.conn.commit()
        self.conn.close()

    def process_item(self, meal, spider):
        if not (meal["description"] and meal["kind"] and meal["date"] and meal["mensa"]):
            raise DropItem("Not a valid item. ")
        else:
            try:
                self.c.execute("INSERT OR IGNORE INTO kind (name) VALUES (?)", (meal["kind"][0], ))
                self.c.execute("INSERT OR IGNORE INTO meal (description, kind) VALUES (?,?)", (meal["description"][0], meal["kind"][0]))
                self.c.execute("INSERT OR IGNORE INTO mensa (name) VALUES (?)", (meal["mensa"][0], ))
                if meal["food_lables"]:
                    lable_insert(self.c, meal["description"][0], meal["food_lables"])

                if meal["special"]:
                    lable_insert(self.c, meal["description"][0], meal["special"][0].split(", "))
                if meal["allergenes"]:
                    lable_insert(self.c, meal["description"][0], meal["allergenes"][0][11:].split(", "))
                if meal["additives"]:
                    lable_insert(self.c, meal["description"][0], meal["additives"][0][14:].split(", "))

                self.c.execute("INSERT OR IGNORE INTO mensa_has_meal (meal,mensa,avail_date,price_student,price_employee,price_guest,avail_time) VALUES (?,?,?,?,?,?,?)", (meal["description"][0], meal["mensa"][0], date_generator(meal["date"][0]), meal["price_student"][0][:4], meal["price_employee"][0][:4], meal["price_guest"][0][:4],meal["date"][0][-12:]))

                self.conn.commit()

            except sqlite3.Error as e:
                print("---- SQL ---- ", e.args[0], meal)

            return meal
