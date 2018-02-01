# -*-coding: utf-8 -*-

"""
# 说明：对企业这个类进行集中处理
"""

from printer import DB


class Company(DB.Model):
    """企业信息的model"""
    __tablename__ = 'company'
    id = DB.Column(DB.Integer, primary_key=True)
    company = DB.Column(DB.String(255), unique=True)
    province = DB.Column(DB.String(255))
    city = DB.Column(DB.String(255))
    name = DB.Column(DB.String(255))
    position = DB.Column(DB.String(255))
    mobile = DB.Column(DB.String(255))
    landline = DB.Column(DB.String(255))

    def __init__(self, company, province, city, name, position, mobile, landline):
        self.company = company
        self.province = province
        self.city = city
        self.name = name
        self.position = position
        self.mobile = mobile
        self.landline = landline

    def __repr__(self):
        return '<Company %r>' % self.company
