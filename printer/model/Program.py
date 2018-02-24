# -*-coding: utf-8 -*-

"""
# 说明：对Program这个类进行集中处理
"""

from printer import DB


class Program(DB.Model):
    """定制方案的model"""
    __tablename__ = 'program'
    customer_id = DB.Column(DB.Integer, DB.ForeignKey('company.id'))
    program_id = DB.Column(DB.Integer, primary_key=True, autoincrement=True, nullable=False)
    painting_id = DB.Column(DB.Integer, DB.ForeignKey('painting.id'))
    product_id = DB.Column(DB.Integer, DB.ForeignKey('product.id'))
    painting_program = DB.Column(DB.Integer)
    device_program = DB.Column(DB.Integer)
    dry_program = DB.Column(DB.Integer)


    def __init__(self, customer_id, product_id, painting_id, painting_program, device_program, dry_program):
        self.customer_id = customer_id
        self.product_id = product_id
        self.painting_id = painting_id
        self.painting_program = painting_program
        self.device_program = device_program
        self.dry_program = dry_program

    def __repr__(self):
        return '<Company %r>' % self.program_id
