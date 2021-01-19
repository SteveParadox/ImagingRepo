from flask import Flask, render_template, redirect, request, url_for, Blueprint, abort
import uuid
from .models import Upload, Users
from utils import save_img
from form import Register, Store
from dev import db
from flask_login import current_user, login_required, login_user
from werkzeug.security import check_password_hash, generate_password_hash

load = Blueprint('load', __name__)


@load.route('/login', methods=['GET', 'POST'])
def login():
    form = Register()
    user = Users.query.filter_by(email=request.form.get('name')).first()
    if user:
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            return redirect(url_for('load.upload'))
        return redirect(url_for('load.login'))
    else:
        if form.validate_on_submit():
            user = Users()
            user.name=form.name.data
            user.password=generate_password_hash(form.password.data)
            db.session.add(user)
            db.session.commit()
            user = Users.query.filter_by(email=request.form.get('name')).first()
            login_user(user, remember=True)
            return redirect(url_for('load.upload')) 
    return render_template('', form=form)



@load.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    imageUser= Upload.query.filter_by(data=current_user).order_by(Upload.dateUploaded.desc()).all()
    imageAll= Upload.query.order_by(Upload.dateUploaded.desc()).all()
    for storeForm in Store():
        form = storeForm
        if form.validate_on_submit():
            name = str(form.name.data)
            image = save_img(form.image.data)
            imageFile = request.files['image']
            upload = Upload(data=current_user)
            upload.name = name
            upload.image = image
            upload.publicId = uuid.uuid4()
            upload.imageData = imageFile.read()
            db.session.add()
            db.session.commit()
            return redirect(url_for('load.upload'))
      
    return render_template('', imageUser=imageUser, imageAll=imageAll, form=form)

@load.route('/delete/<string:publicId>', methods=['GET', 'POST'])
@login_required
def deleteOne(publicId):
    imageDel= Upload.query.filter_by(publicId=publicId).first()
    if imageDel.data != current_user:
        abort(403)
    db.session.delete(imageDel)
    db.session.commit()
    return redirect(url_for('load.upload'))


@load.route('/delete', methods=['GET', 'POST'])
@login_required
def deleteAll():
    imageDel= Upload.query.filter_by(data=current_user).all()
    if imageDel.data != current_user:
        abort(403)
    for files in imageDel:
        db.session.delete(files)
    db.session.commit()
    return redirect(url_for('load.upload'))
