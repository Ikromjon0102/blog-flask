import hashlib
from flask import render_template, request, redirect, url_for, flash
from articles import Article
import os
from slugify import slugify
from articles import Article

from flask import (
    Flask, 
    render_template, 
    request, 
    make_response, 
    session, 
    redirect
    )

app = Flask(__name__)
app.secret_key = "thisisverysecret"


users = {
    "admin" : "5e6da379640e775890b4067b3cbea9d13a6bb321b32f7f3442b53b6cc989d596"
}



@app.route('/')
def blog():
    articles = Article.all()
    return render_template("blog.html", articles = articles)




@app.route("/publish")
def publish_page():
    if "user" not in session:
        return redirect("/admin")
    
    return render_template("publish.html")


# =========== chatgpt ========


@app.route("/publish", methods=["GET", "POST"])
def add_blog():
    if request.method == "POST":
        title = request.form["title"]
        text = request.form["text"]

        article = Article(title)
        article.save_content(text)

        flash("Blog successfully added!")

        return redirect("/")

    return render_template("publish.html")

# =========== chatgpt ========


# @app.post("/publish")
# def add_blog():
#     title = request.form["title"]
#     text = request.form["text"]
#     with open(f"articles/{title}", "w+") as file:
#         body = f"{title}\n {text}"
#         file.write(body)
    
    
#     return "blog muvaffaqiyatli qo'shildi"



@app.get("/admin")
def admin_page():
    if "user" in session:
        return render_template("publish.html")
    
    return render_template("login.html")

@app.get("/logout")
def logout():
    del session["user"]
    return "you are logout"
    

@app.post("/admin")
def admin_login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username not in users:
        return render_template("login.html", error="username or password incorrect")
    hashed = hashlib.sha256(password.encode()).hexdigest()
    
    if users.get(username) != hashed:
        return render_template("login.html", error="nimadir xato")
    
    session["user"] = username
    return "you are authenticated"


@app.route('/set-session')
def set_session():
    session["user_id"] = 1
    return "session set"

@app.route('/get-session')
def get_session():
    session["user_id"] = 1
    return f"user_id = {session.get("user_id")}"

@app.route('/first-time')
def first_time():
    if 'seen' not in request.cookies:
        response = make_response("You are new here")
        response.set_cookie("seen", "1")
        return response

    seen = int(request.cookies['seen'])
    response = make_response(f"I have seen you before {seen} times")
    response.set_cookie("seen", str(seen+1))
    return response

@app.route("/blog/<slug>/")
def article(slug: str):
    articles = Article.all()
    article = articles[slug]
    return render_template("salom.html", article=article)


if __name__ == '__main__':
    app.run(port=4200, debug=True)
