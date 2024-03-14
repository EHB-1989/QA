import sqlite3
from flask import Flask
from item import Item
import time



sql_create_items_table = """ CREATE TABLE IF NOT EXISTS items (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        description text
                                    ); """

# class Item(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     description = db.Column(db.String(200))

class DBManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.connection.execute(sql_create_items_table)
        self.connection.commit()

    def get_db_conn(self):
        return self.connection

    def add_item(self, item:Item):
        self.connection.execute('INSERT INTO items (name, description) VALUES (?, ?)', (item.name, item.description))
        self.connection.commit()

    def get_item(self):
        cursor = self.connection.execute('SELECT name, description FROM items')
        return [Item(name, description) for name, description in cursor]

    def __del__(self):
        self.connection.close()

    
   