import sqlite3

def connection():
    c = sqlite3.connect('database.db')
    return c.cursor()