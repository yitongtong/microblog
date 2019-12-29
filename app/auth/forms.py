from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住登录')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    password2 = PasswordField(
        '确认密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('注册')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    submit = SubmitField('提交')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('新密码', validators=[DataRequired()])
    password2 = PasswordField(
        '确认新密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('重制密码')
