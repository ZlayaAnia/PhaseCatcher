from web_app import db, create_app

db.create_all(app=create_app())