# -*- coding:utf-8 -*-
'''
# 说明： 配置信息
'''

#调试模式是否开启
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
# session 必须要设置key, 暂时不需要
# SECRET_KEY = 'Adsadsoa'

# mysql数据库连接信息
SQLALCHEMY_DATABASE_URI = 'mysql://root:q52013142@localhost:3306/recommend'
