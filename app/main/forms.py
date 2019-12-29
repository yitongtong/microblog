from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    about_me = TextField('个人介绍', validators=[Length(min=0, max=140)])
    submit = SubmitField('提交')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username')


class PostForm(FlaskForm):
    post = TextAreaField('说点什么吧。。。', validators=[
                         DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('提交')
