from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    print("🔥 Contact form submitted (MongoDB disabled)")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)