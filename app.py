from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    success = False
    username = ""
    email = ""

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        success = bool(username and email and "@" in email)

    return render_template(
        "index.html",
        success=success,
        username=username,
        email=email,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
