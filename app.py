from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
client.admin.command("ping")

db = client["portfolio_db"]
contacts = db["contacts"]

print("✅ MongoDB Connected Successfully")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():

    print("🔥 CONTACT ROUTE HIT")

    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    data = {
        "name": name,
        "email": email,
        "message": message
    }

    result = contacts.insert_one(data)

    print("✅ Saved")
    print(result.inserted_id)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)