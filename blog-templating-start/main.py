from flask import Flask, render_template
from post import Post

app = Flask(__name__)
blog_post = Post()

@app.route('/')
def home():
    return render_template("index.html", posts=blog_post.get_posts())

@app.route('/post/<int:post_id>')
def post(post_id): 
    return render_template("post.html", post=blog_post.get_post_via_id(post_id))

if __name__ == "__main__":
    app.run(debug=True)
