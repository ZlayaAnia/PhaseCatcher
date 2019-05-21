import os
import sys
import requests

from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, send_from_directory, url_for  
from werkzeug.utils import secure_filename

from web_app.forms import DownloadForm
from web_app.model import db, Experiment, Files


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'bmp', 'jpg', 'jpeg', 'gif'])


basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(basedir, 'uploads')

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.Exception, ValueError):
        print('Сетевая ошибка')
        return False

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(user_id):
    if request.method == 'POST':
        x = request.files
        if 'upload' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['upload']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            uploaded = datetime.now()
            print(uploaded, file=sys.stdout)
            print(filename, file=sys.stdout)
            save_file(filename, user_id)
            print('!!!', file=sys.stdout)
            return filename

def analise_file(user_id, form):
    experiment_time = datetime.now()
    experiment_2_db = Experiment(name='name', sample_name=form.sample_name, 
                                 alloy_name=form.alloy_name, comment=form.comment,
                                 experiment_time=experiment_time, image_scale=form.image_scale, 
                                 particle='particle', average_size='average_size', 
                                 deviation_size='deviation_size', shape_parametr='shape_parametr', 
                                 particles_number='particles_number', image_wb=form.image_wb_min)
    db.session.add(experiment_2_db)
    db.session.commit()

def save_file(file_name, user_id):
    uploaded = datetime.now()
    file_exists = Files.query.filter(Files.file_name == file_name).count()
    if not file_exists:
        file_2_db = Files(file_name=file_name, uploaded=uploaded, user_id=user_id)
        print('@'*11, file=sys.stderr)
        db.session.add(file_2_db)
        print('@'*11, file=sys.stderr)
        db.session.commit( )
    else:
        print('ФАЙЛ УЖЕ ЕСТЬ')
        pass

def all_files(files):
    print('!!!!!', file=sys.stderr)
    files = Files.query.all()
    print(files, file=sys.stderr)
    if not files:
        return('В базе нет файлов')
