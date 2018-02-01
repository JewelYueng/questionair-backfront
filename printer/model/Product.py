# -*-coding: utf-8 -*-

"""
# 说明：对Product这个类进行集中处理
"""

from printer import DB


class Product(DB.Model):
    """企业信息的model"""
    __tablename__ = 'product'
    id = DB.Column(DB.Integer, primary_key=True)
    custom_id = DB.Column(DB.Integer, DB.ForeignKey('company.id'))
    style = DB.Column(DB.String(255))
    type = DB.Column(DB.String(255))
    base = DB.Column(DB.String(255))

    def __init__(self, custom_id, style, type, base):
        self.custom_id = custom_id
        self.style = style
        self.type = type
        self.base = base

    def __repr__(self):
        return '<Product %r>' % self.custom_id
