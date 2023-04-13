"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrqagvdvk4rjsvb1fvg-a.oregon-postgres.render.com",
        database="todo_kk3g",
        user="root",
        password="Kc1ckA6r7uXsk3jcie3Xtnz73I4rAznh")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
