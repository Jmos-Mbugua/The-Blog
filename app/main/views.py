from flask import render_template,url_for,request,flash,redirect,abort
from app.main  import main
from app.models import User,Blog,Comment, Subscriber
from .. import db, photos
from .forms import UpdateProfile,CreateBlog
from flask_login import login_required,current_user
import secrets
import os
# from PIL import Image
from ..email import mail_message
from ..request import get_quote

@main.route('/')
def index():
    page = request.args.get('page',1,type =int)
    blogs = Blog.query.order_by(Blog.posted.desc()).paginate(page = page,per_page = 3)
    quote = get_quote()
    return render_template('index.html',blogs=blogs, quote = quote)

@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
        
    return redirect(url_for('main.profile', uname = uname))


@main.route('/user/<username>',methods=['GET','POST'])
def profile(username):
    user = User.query.filter_by(username = username).first()
    
    if user is None:
        abort(404)
        
    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/new_post',methods=['GET','POST'])
@login_required
def new_blog():
    subscribers = Subscriber.query.all()
    form = CreateBlog()
    if form.validate_on_submit():
        title = form.title.data
        user_id = current_user._get_current_object().id
        content = form.content.data
        blog = Blog(title = title, content = content,user_id=user_id)
        blog.save_blog()
        for subscriber in subscribers:
            mail_message('New blog post','email/new_blog',subscriber.email,blog=blog)
        return redirect(url_for('main.index'))
    return render_template('newblog.html',form = form)

@main.route('/blog/<id>')
def post(id):
    comments = Comment.query.filter_by(blog_id = id).all()
    blog = Blog.query.get_or_404(id)
    return render_template('blog.html',blog = blog ,comment= comments)

@main.route('/blog/<blog_id>/update',methods=['GET','POST'])
@login_required
def updateblog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(404)
    form = CreateBlog()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.content = form.content.data
        db.session.commit()
        flash('You have updated your Blog')
        return redirect(url_for('main.index',id=blog_id))
    if request.method == 'GET':
        form.title.data = blog.title
        form.content.data = blog.content
    return render_template('newblog.html',form = form)

@main.route('/comment/<blog_id>',methods=['GET','POST'])
def comment(blog_id):
    blog = Blog.query.get(blog_id)
    comment = request.form.get('newcomment')
    new_comment = Comment(comment = comment, user_id = current_user._get_current_object().id, blog_id=blog_id)
    new_comment.save_comment()
    return redirect(url_for('main.blog',id= blog.id))

@main.route('/blog/<blog_id>/delete', methods=['POST'])
@login_required
def del_post(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    db.session.delete(blog)
    db.session.commit()

    flash('You have deleted your Blog succesfully')
    return redirect(url_for('main.index'))

@main.route('/user/<string:username>')
def user_post(username):
    user = User.query.filter_by(username=username).first()
    page = request.args.get('page',1,type = int)
    blogs = Blog.query.filter_by(user = user ).order_by(Blog.posted.desc()).paginate(page = page,per_page=4)
    return render_template('userpost.html',blogs=blogs,user=user)