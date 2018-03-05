# -*- coding:utf-8 -*-
"""
# 名称： program_handler.py
# 作用：进行路由处理
"""

import time
from printer import APP,DB
from printer.model.Company import Company
from printer.model.Painting import Painting
from printer.model.Product import Product
from printer.model.Program import Program
from flask import request, jsonify, render_template

@APP.route('/')
def index():
    return render_template('index.html')

@APP.route('/check/company', methods=["GET"])
def check_company():
    """检验企业名称是否已经存在"""
    # 这里需要检验是否在数据库中已经存在相应的企业名称
    company = Company.query.filter_by(company = request.args['company']).first()
    return jsonify({'isExit': company != None})

@APP.route('/check/name', methods=['GET'])
def check_name():
    """检验企业联系人是否已经存在"""
    #这里需要检验是否在数据库中已经存在相应的企业联系人
    name = Company.query.filter_by(name=request.args['name']).first()
    return jsonify({'isExit': name != None})

@APP.route('/check/mobile', methods=['GET'])
def check_mobile():
    """检验手机号码是否已经存在"""
    mobile = Company.query.filter_by(mobile=request.args['mobile']).first()
    return jsonify({'isExit': mobile != None})

@APP.route('/check/landline', methods=['GET'])
def check_landline():
    """检验座机号码是否已经存在"""
    landline = Company.query.filter_by(landline=request.args['landline']).first()
    return jsonify({'isExit': landline != None})

@APP.route('/addClient', methods=['POST'])
def add_client():
    """处理前端传来的提交企业信息"""
    infoForm = request.json['clientInfo']
    productForm = request.json['product']
    paintingForm = request.json['painting']

    newCom = Company(infoForm['company'], infoForm['province'], infoForm['city'], infoForm['name'], infoForm['position'], infoForm['mobile'], infoForm['landline'])
    DB.session.add(newCom)
    DB.session.commit()

    company_id = newCom.id

    product = Product(company_id, productForm['style'], productForm['type'], productForm['base'])
    paint = Painting(company_id, paintingForm['amount'], paintingForm['effect'], paintingForm['luster'], paintingForm['program'], paintingForm['workpiece'])

    DB.session.add(product)
    DB.session.add(paint)
    DB.session.commit()

    if paintingForm['program'] == 1:
        program = Program(company_id, product.id, paint.id, paintingForm['effect'], paintingForm['workpiece'], 0)
    else:
        program = Program(company_id, product.id, paint.id, paintingForm['effect'], 0, paintingForm['workpiece'])

    DB.session.add(program)
    DB.session.commit()

    DB.session.commit()
    return jsonify({
        'pid': program.program_id
    })

@APP.route('/client', methods=['POST'])
def get_client():
    program_id = request.json['pid']
    program = Program.query.filter_by(program_id = program_id).first()

    product = Product.query.filter_by(id=program.product_id).first()
    painting = Painting.query.filter_by(id=program.painting_id).first()
    customer = Company.query.filter_by(id=program.customer_id).first()

    return jsonify({
        'proCode': '%s%d' % (time.strftime('%y%m%d', time.localtime(time.time())), program.program_id),
        'customer': {
            'company': customer.company,
            'name': customer.name,
            'phone': customer.mobile
        },
        'product': {
            'style': product.style,
            'type': product.type,
            'base': product.base,
            'effect': painting.effect,
            'program':painting.program,
            'workpiece': painting.workpiece,
            'luster': painting.luster
        },
        'program': {
            'painting': painting.effect,
            'method': '%d, %d' % (program.dry_program == 0, painting.workpiece)
        }
    })

