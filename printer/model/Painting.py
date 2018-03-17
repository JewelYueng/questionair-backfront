# -*-coding: utf-8 -*-

"""
# 说明：对Painting这个类进行集中处理
"""

from printer import DB


class Painting(DB.Model):
    """涂料信息的model"""
    __tablename__ = 'painting'
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    customer_id = DB.Column(DB.Integer, DB.ForeignKey('company.id'), primary_key=True)
    amount = DB.Column(DB.Integer)
    effect = DB.Column(DB.Integer)
    luster = DB.Column(DB.String(9))
    program = DB.Column(DB.Integer)
    workpiece = DB.Column(DB.Integer)
    lusterStr = DB.Column(DB.String(255))

    def __init__(self, customer_id, amount, effect, luster, luster_str,program, workpiece):
        self.customer_id = customer_id
        self.amount = amount
        self.effect = effect
        self.luster = luster
        self.lusterStr = luster_str
        self.program = program
        self.workpiece = workpiece

    def __repr__(self):
        return '<Painting %r>' % self.customer_id
