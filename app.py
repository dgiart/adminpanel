# This is a sample Python script.
from flask import Flask, render_template
from config import Configuration
from time import time, asctime
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
app = Flask(__name__)
app.config.from_object(Configuration)
import sys



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
