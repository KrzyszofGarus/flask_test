from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
db = {
    "a":"blob post 1", 
    "b":"blog post 2",
    "c":"blog post 3"
    }

    

@app.route("/")
def hello_world():
    return render_template("index.html", db = db)

@app.route("/test")
def another_hello():
    return "<p>Hello Fortnite!</p>"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/post/<blog_key>')
def show_post_str(blog_key):
    blog_post = db[blog_key]
    return render_template("blog_post.html", blog_post = blog_post)
     