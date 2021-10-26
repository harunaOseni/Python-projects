from flask import Flask, render_template
from post import Post
from flask import request
import smtplib

app = Flask(__name__)
blog_post = Post()


@app.route('/')
def home():
    return render_template("index.html", posts=blog_post.get_posts())


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        #name, email, phone, message
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.starttls()
            smtp.login('', '')
            subject = "Acquisition Blog Form Entry"
            body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            msg = f"Subject: {subject}\n\n{body}"
            smtp.sendmail('harunaoseni23@gmail.com', 'harunaoseni23@gmail.com', msg)

        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template("post.html", post=blog_post.get_post_via_id(post_id))


if __name__ == "__main__":
    app.run(debug=True)
