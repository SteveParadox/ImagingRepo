import os
import cloudinary as Cloud


class Config:
    def __init__(self):
        pass

    ENV = 'dev'

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
        SQLALCHEMY_DATABASE_URI = "postgres://tmezmgejayycxt:96acdc27bfed485a4d2b4533ac7455e2985763907c71a171edf79a9529c8e3a8@ec2-34-202-65-210.compute-1.amazonaws.com:5432/dbgri8ojt9m5pe"
        DROPZONE_UPLOAD_MULTIPLE = True
        DROPZONE_ALLOWED_FILE_CUSTOM = True
        DROPZONE_ALLOWED_FILE_TYPE = 'image/*'
        DROPZONE_REDIRECT_VIEW = 'results'  
        Cloud.config(
            cloud_name='dc1qkmsr0',
            api_key='223398319444964',
            api_secret='ZzoX3c3Y2mn2PiALJ8RgljfezuM'
        )
