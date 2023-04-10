"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpr5c5269v5rj89t0dg-a",
        database="todo_0qka",
        user="root",
        password="sKZ6DIuUoj2a5UkTdOyIi2NpqvR5Rphy")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
