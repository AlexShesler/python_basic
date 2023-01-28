from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", endpoint="index_page")
def index():
    return render_template("index.html")


@app.route("/about/", endpoint="about_page")
def get_about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
