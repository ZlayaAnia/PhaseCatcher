from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], 
                        render_kw={'class': 'form-control'})
    password = PasswordField('Пароль', validators=[DataRequired()], 
                        render_kw={'class': 'form-control'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-info'})


class RegistrForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], 
                        render_kw={'class': 'form-control'})
    password1 = PasswordField('Пароль', validators=[DataRequired()], 
                        render_kw={'class': 'form-control'})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired()], 
                        render_kw={'class': 'form-control'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-info'})


class DownloadForm(FlaskForm):
    sample_name = StringField('Название образца', validators=[DataRequired()], 
                        render_kw={'class': 'form-control'})
    alloy_name = StringField('Название сплава', validators=[DataRequired()], 
                        render_kw={'class': 'form-control'})
    comment = StringField('Описание образца', validators=[DataRequired()], 
                        render_kw={'class': 'form-control'})
    submit_upload = SubmitField('Загрузить', render_kw={'class': 'btn btn-info'})
    image_scale = StringField('Увеличение при съемке', 
                        validators=[DataRequired()], render_kw={'class': 'form-control'})
    image_wb = StringField('Бинаризация')
    particle = StringField('Выбор частиц')


class ProjectsForm(FlaskForm):
    use_all_experiments = SubmitField('Открыть все', render_kw={'class': 'btn btn-info'})
    use_experiment = SubmitField('Открыть', render_kw={'class': 'btn btn-info'})


