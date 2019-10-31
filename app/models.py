from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio  = db.Column(db.String(255),default='My default Bio')
    profile_pic_path = db.Column(db.String(255),default='default.png')
    pass_secure = db.Column(db.String(255))
    blog = db.relationship('Blog',backref='user',lazy='dynamic')
    comment = db.relationship('Comment',backref='user',lazy='dynamic')

    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'
    
    
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'
    
    
class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    title =  db.Column(db.String(255),nullable = False)
    content = db.Column(db.Text(),nullable = False)
    posted = db.Column(db.DateTime,default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship('Comment',backref='blog',lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.add(self)
        db.session.commit()

    # @classmethod
    def get_blog(self,id):
        blog = Blog.query.filter_by(id=id).first()
        return blog

    def __repr__(self):
        return f'Blog {self.title}'
    
    
class Comment(db.Model):
    
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key =True)
    comment = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default = datetime.utcnow)
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_commit(self):
        db.session.add(self)
        db.session.commit()

    # @classmethod
    def get_comment(self,id):
        comment = Comment.query.all(id=id)
        return comment

    def __repr__(self):
        return f'Comment {self.comment}'
    
    
class Subscriber(db.Model):
    __tablename__='subscribers'

    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'
    
    
class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))


    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls,id):
        upvote = Upvote.query.filter_by(blog_id = id).all()
        return upvote

    def __repr__(self):
        return f"{self.user_id}:{self.blog_id}"
    
    
class Downvote(db.Model):
    __tablename__ = 'downvotes'

    id =  db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls,id):
        downvotes = Downvote.query.filter_by(blo_id = id).all()
        return downvotes

    def __repr__(self):
        return f"{self.user_id}:{self.blog_id}"
    
    
class Quote:
    """
    Class with quotes consumed from the quotes api
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote
    