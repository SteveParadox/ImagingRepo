# importing libraries
import os
import cloudinary as Cloud

# app configuration
class Config:

    ENV = 'prod'

    if ENV == 'dev':
        SECRET_KEY = "43rtgtrf04o0gkomrg0gmr0gtgmg0trgo"
        SQLALCHEMY_DATABASE_URI = 'sqlite:///store.db'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        DROPZONE_UPLOAD_MULTIPLE = True
        DROPZONE_ALLOWED_FILE_CUSTOM = True
        DROPZONE_ALLOWED_FILE_TYPE = 'image/*'
        DROPZONE_REDIRECT_VIEW = 'load.upload'    
        UPLOADED_PHOTOS_DEST = os.getcwd() + '/static'

    else:
        SECRET_KEY = "795849f0d2328258710ae9c71cb795849f0d2328258710ae9c71cb4b5ea4b5ea"
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SQLALCHEMY_DATABASE_URI = "postgres://wivhavfezhmnia:3fde540c0f2b5744235c6e9d0f181a92101ec85b5fda29b2136d41b3a2873f90@ec2-52-70-67-123.compute-1.amazonaws.com:5432/d8jbm55mvars4k"
        DROPZONE_UPLOAD_MULTIPLE = True
        DROPZONE_ALLOWED_FILE_CUSTOM = True
        DROPZONE_ALLOWED_FILE_TYPE = 'image/*'
        DROPZONE_REDIRECT_VIEW = 'load.upload'    
        UPLOADED_PHOTOS_DEST = os.getcwd() + '/static'
        Cloud.config(
            cloud_name='dc1qkmsr0',
            api_key='223398319444964',
            api_secret='ZzoX3c3Y2mn2PiALJ8RgljfezuM'
        )
