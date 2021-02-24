# importing libraries
from flask import Flask, render_template, redirect, request, url_for, Blueprint, abort, jsonify # importing libraries from framework
import uuid # using random string generator
from ..models import Upload, Users # importing classes from models.py 
from .utils import save_img # importing image processing class from utils.py
from .form import Register # importing forms from forms.py
from dev import db, app # importing database and app configuration from folder package
from flask_login import current_user, login_required, login_user # using flask login
from werkzeug.security import check_password_hash, generate_password_hash # using flask security
from flask_uploads import IMAGES,   UploadSet, configure_uploads, patch_request_class # using flask uploads
from .. import dropzone

# registering blueprint 
load = Blueprint('load', __name__)

# flask uploads config for app
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)




# logging in to app
@load.route('/login', methods=['GET', 'POST'])
def login():
    # using created form class Register
    form = Register()
    # checking if entered name is already registered
    user = Users.query.filter_by(name=request.form.get('name')).first()
    
    if user:
        # if already registered check if password matches
        if user and check_password_hash(user.password, form.password.data):
            # if password matches the name, log user in 
            login_user(user, remember=True)
            return redirect(url_for('load.upload'))
        # if it does not match go back to login page
        return redirect(url_for('load.login'))
    # if name is not already registered, registers user and log user in
    else:
        if form.validate_on_submit():
            user = Users()
            user.name=form.name.data
            user.password=generate_password_hash(form.password.data)
            db.session.add(user)
            db.session.commit()
            user = Users.query.filter_by(name=request.form.get('name')).first()
            login_user(user, remember=True)
            return redirect(url_for('load.upload')) 
    return render_template('login.html', form=form)


# uploading images
@load.route('/', methods=['GET', 'POST'])
@login_required
def upload():
    # getting all uploaded images from the database
    imageAll= Upload.query.order_by(Upload.dateUploaded.desc()).all()
    # check if server is making a post request
    if request.method == 'POST':
        file_obj = request.files
        # loop through uploaded files and commit them to the database
        for f in file_obj:
            file = request.files.get(f)
            print (file.filename)
            image = save_img(file)
            upload = Upload(data=current_user)
            upload.name = file.filename
            upload.image = image 
            upload.publicId = str(uuid.uuid4())
            db.session.add(upload)
            db.session.commit()

        return "uploading..."
      
    return render_template('upload.html', imageAll=imageAll)

# deleting a single image
@load.route('/delete/<string:publicId>', methods=['GET', 'POST'])
@login_required
def deleteOne(publicId):
    # gets the public id of the image and compare it against the public ids in the database
    # then checks if the registered uploader is the current active user accessing it
    imageDel= Upload.query.filter_by(publicId=publicId).filter_by(data=current_user).first()
    # if it is the registered uploader then authorization is given to delete it
    if imageDel:
        db.session.delete(imageDel)
        db.session.commit()
        return redirect(url_for('load.upload'))
    # if not registered uploader then user is blocked
    return jsonify({
        "message": "You are not authorized to delete this"
    })

# deleting all images of a registered user
@load.route('/delete', methods=['GET', 'POST'])
@login_required
def deleteAll():
    # searches for all the images of a particular registered user
    imageDel= Upload.query.filter_by(data=current_user).all()
    # deletes them
    for files in imageDel:
        db.session.delete(files)
    db.session.commit()
    return redirect(url_for('load.upload'))
