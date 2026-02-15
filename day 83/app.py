from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

PROJECTS = [
    {
        "title": "MERN Travel Blog",
        "description": "Full-stack social media driven travel platform.",
        "link": "https://github.com/VedanthGit/Social-Media-Driven-Travel-Blogging-Platform.git",
    },
    {
        "title": "Ghost Typer Game",
        "description": "Horror-themed typing game with animations.",
        "link": "https://github.com/VedanthGit/ghost-typer.git",
    },
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        print(name, email, message)
        return redirect(url_for("home"))
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
