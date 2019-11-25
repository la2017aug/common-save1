import os
from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
from db.database import DB
from models import Supermarket


supermarkets = Blueprint('supermarkets', __name__,
                         url_prefix='/supermarket',
                         template_folder='../supermarkets/templates',
                         static_folder='../supermarkets/static')


@supermarkets.route('/', methods=['GET'])
def get_all_supermarkets():
    supermarkets_all = [supermarket.__dict__ for supermarket in DB['supermarkets']]
    args = request.args.to_dict()
    return render_template('all_supermarkets.html',
                           supermarkets_all=supermarkets_all, args=args)


@supermarkets.route('/add', methods=['GET'])
def show_add_supermarket_form():
    return render_template('add_supermarket.html')


@supermarkets.route('/', methods=['POST'])
def add_supermarket():
    data = request.form.to_dict()
    file = request.files['img_name']
    if file:
        filename = secure_filename(file.filename)
        path_to_img = os.path.join('supermarkets/static',
                                   secure_filename(filename)
                                   )
        file.save(path_to_img)
    else:
        filename = None
    DB['supermarkets'].append(Supermarket(name=data.get('name'),
                                          location=data.get('location'),
                                          img_name=filename
                                          )
                              )
    return redirect(url_for('supermarkets.get_all_supermarkets'))


@supermarkets.route('/<uuid:uu_id>')
def show_supermarket(uu_id):
    uu_id = str(uu_id)
    supermarkets_all = [supermarket.__dict__ for supermarket in DB['supermarkets']]
    supermarket_to_show = None
    for supermarket in supermarkets_all:
        if uu_id in supermarket.values():
            supermarket_to_show = supermarket
    return render_template('supermarket.html', supermarket=supermarket_to_show)
