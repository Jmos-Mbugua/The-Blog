from flask_wtf import FlaskForm 
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Email,Required
from flask_login import current_user
from ..models import User

class UpdateProfile(FlaskForm):
    username =StringField('Enter You Name',validators =[Required()])
    email =StringField('Enter You Email',validators =[Required(),Email()])
    bio =TextAreaField('Write a brief about yourself',validators =[Required()])
    profile_pic = FileField('profile picture',validators =[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')


    def validate_email(self,email):
        if email.data != current_user.email:
            if User.query.filter_by(email = email.data).first():
                raise ValidationError("The Email has already been taken!")
    def validate_username(self,username):
        if username.data != current_user.username:
            if User.query.filter_by(username = username.data).first():
                raise ValidationError("The username has already been taken")

class CreateBlog(FlaskForm):
    title = StringField('Title',validators=[Required()])
    content = TextAreaField('Blog content',validators=[Required()])
    submit = SubmitField('Post')