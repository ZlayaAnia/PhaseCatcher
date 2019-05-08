import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
print(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'bmp'])
SECRET_KEY = "asdasfasfafafasfasf"
