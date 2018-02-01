# -*- coding:utf-8 -*-
'''
# 说明：进行模块的初始化
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_cors import *

pymysql.install_as_MySQLdb()

# 创建项目对象
APP = Flask(__name__)
# 家在配置文件内容
APP.config.from_object('printer.setting')
APP.config.from_envvar('FLASK_SETTING')
# 创建数据库对象
DB = SQLAlchemy(APP)
CORS(APP, suports_credentials=True)
from printer.model import Company, Painting, Product, Program
from printer.controller import program_handler

