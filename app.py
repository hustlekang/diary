from flask import Flask,render_template, request,url_for,redirect,session,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.elements import Null
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='secretkey'

db=SQLAlchemy(app)


class user(db.Model):
    user_id=db.Column(db.String(10), primary_key=True)
    user_pw=db.Column(db.String(10), nullable=False)
    user_email=db.Column(db.String(30), nullable=False)

    def __init__(self,user_id,user_pw,user_email):
        self.user_id=user_id
        self.user_pw=user_pw
        self.user_email=user_email

    def __repr__(self):
        return "<User('%s','%s','%s')>"%(self.user_id,self.user_pw,self.user_email)

class Post(db.Model):
    image=db.Column(db.Text())
    comment=db.Column(db.Text())
    user_id=db.Column(db.String(10))
    post_id=db.Column(db.Integer,primary_key=True)

    def __init__(self,image,comment,user_id):
        self.user_id=user_id
        self.image=image
        self.comment=comment

    def edit_image(self,image):
        self.image=image
    def edit_comment(self,comment):
        self.comment=comment

    def __repr__(self):
        return "<Post('%s','%s','%s','%d')>"%(self.image,self.comment,self.user_id,self.post_id)

@app.route('/upload',methods=['POST'])
def upload():
    return render_template('upload.html')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        return render_template('signup.html')

@app.route('/check_signup',methods=["POST"])
def check_signup():
    if request.form['id']=="" or request.form['pw']=="" or request.form['email']=="" or request.form['pw2']=="":
        flash("fill it everything")
        return render_template("signup.html")

    else:
        if request.form['pw']==request.form['pw2']:
            user_=user(request.form['id'],request.form['pw'],request.form['email'])
            db.session.add(user_)
            db.session.commit()
            flash("Welcome")
            return render_template("login.html")
        else:
            flash("confirm pw")
            return render_template("signup.html")

@app.route('/upload_post',methods=["POST"])
def upload_post():
    if request.files['file'].filename=="" and request.form['comment']=="":
        flash("choose picture and write down comment")
        return render_template('upload.html')
    elif  request.files['file'].filename=="":
        flash("choose picture ")
        return render_template('upload.html')
    elif request.form['comment']=="" :
        flash("write down comment")
        return render_template('upload.html')
    else:
        post_= Post(request.files['file'].filename,request.form['comment'],session['user_id'])
        img=request.files["file"]
        img.save("./static/"+secure_filename(img.filename))
        db.session.add(post_)
        db.session.commit()
        flash("Uploaded")
        return redirect(url_for('main'))



@app.route('/check_user',methods=["POST"])
def check_user():
    if db.session.query(user.query.filter(user.user_id==request.form['id'],user.user_pw==request.form['pw']).exists()).scalar():
        session['user_id']=request.form['id']
        return redirect(url_for('main'))
    else:
        flash("Check Info")
        return render_template("login.html")

@app.route('/main')
def main():
    post = db.session.query(Post).filter_by(user_id=session['user_id']).all()
    user_id=session['user_id']+"'s DIARY"
    return render_template("main.html", post=post,user_id=user_id)

@app.route('/delete', methods=['POST'])
def delete():
    db.session.query(Post).filter(Post.post_id==request.form['post_id']).delete()
    db.session.commit()
    flash("Post is deleted")
    return redirect(url_for('main'))

@app.route('/edit',methods=['POST'])
def edit():
    post_id=request.form['post_id']
    post=db.session.query(Post).filter(Post.post_id==post_id).first()
    image=post.image
    comment=post.comment
    return render_template("edit.html",comment=comment,image=image,post_id=post_id)

@app.route('/edit_process',methods=['POST'])
def edit_process():
    post_id=request.form['post_id']
    post=db.session.query(Post).filter(Post.post_id==post_id).first()
    post.edit_image(request.files['file'].filename)
    post.edit_comment(request.form['comment'])
    db.session.commit()
    return redirect(url_for('main'))

@app.route('/logout',methods=["POST"])
def logout():
    session.pop("user_id",None)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

