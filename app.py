from flask import Flask, render_template
from dotenv import load_dotenv
from extensions import db
import os

load_dotenv()

app = Flask(__name__)

user = os.getenv("database_user")
password = os.getenv("database_password")
host = os.getenv("database_host")
db_name = os.getenv("database_name")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{user}:{password}@{host}/{db_name}"
)

# Connect SQLAlchemy with Flask
db.init_app(app)

# Import models
from models import bussiness_data

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=3000)