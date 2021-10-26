from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


db.create_all()

# starbucks_cafe = Cafe(name="Starbucks", map_url="https: // www.starbucks.com/store-locator/store/12562/wakefield-belmont-plaza-600-kingstown-rd-wakefield-ri-028793654-us",
#                       img_url="https://www.starbucks.com/content/dam/starbucks/images/store/locations/belmont-plaza/belmont-plaza-store-locator-hero.jpg", location="Wakefield, RI", seats="150", has_toilet=True, has_wifi=True, has_sockets=True, can_take_calls=True, coffee_price="$1.50")

# db.session.add(starbucks_cafe)
# db.session.commit()


@ app.route("/")
def home():
    return render_template("index.html")


def convRowToDict(row):
    dict = {}
    for column in row.__table__.columns:
        dict[column.name] = str(getattr(row, column.name))

    return dict

# HTTP GET - Read Record


@ app.route("/random", methods=["GET"])
def random():
    # get a radom cafe
    random_cafe = Cafe.query.order_by(db.func.random()).first()
    # return jsonify(
    #     name=random_cafe.name,
    #     map_url=random_cafe.map_url,
    #     img_url=random_cafe.img_url,
    #     location=random_cafe.location,
    #     seats=random_cafe.seats,
    #     amenities = {
    #         "has_toilet": random_cafe.has_toilet,
    #         "has_wifi": random_cafe.has_wifi,
    #         "has_sockets": random_cafe.has_sockets,
    #         "can_take_calls": random_cafe.can_take_calls,
    #     },
    #     coffee_price=random_cafe.coffee_price
    # )
    random_cafe_dict = convRowToDict(random_cafe)
    return jsonify(random_cafe_dict)


@app.route("/all", methods=["GET"])
def all():
    all_cafes = Cafe.query.all()
    all_cafes_dict = [convRowToDict(cafe) for cafe in all_cafes]
    return jsonify(all_cafes_dict)


@app.route("/search", methods=["GET"])
def search():
    # get the search parameter
    search_param = request.args.get("location")
    # search for cafes with the search parameter
    search_cafes = Cafe.query.filter(
        Cafe.location.contains(search_param)).all()
    # return the cafes
    search_cafes_dict = [convRowToDict(cafe) for cafe in search_cafes]
    if len(search_cafes_dict) == 0:
        return jsonify({"error": {
            "Not Found": "Sorry, we don't have a cafe at that location."
        }})
    return jsonify(search_cafes_dict)

# HTTP POST - Create Record


@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        # get the request form data
        name = request.form.get("name")
        map_url = request.form.get("map_url")
        img_url = request.form.get("img_url")
        location = request.form.get("location")
        seats = request.form.get("seats")
        has_toilet = request.form.get("has_toilet")
        has_wifi = request.form.get("has_wifi")
        has_sockets = request.form.get("has_sockets")
        can_take_calls = request.form.get("can_take_calls")
        coffee_price = request.form.get("coffee_price")
        # create a new cafe
        new_cafe = Cafe(name=name, map_url=map_url, img_url=img_url, location=location, seats=seats, has_toilet=has_toilet,
                        has_wifi=has_wifi, has_sockets=has_sockets, can_take_calls=can_take_calls, coffee_price=coffee_price)
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(
            {
                "response": {
                    "success": "Successfully added the new cafe."
                }
            }
        )

# HTTP PUT/PATCH - Update Record


@app.route("/update-price/<int:cafe_id>", methods=["PUT", "PATCH"])
def update_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if request.method == "PATCH":
        coffee_price = request.form.get("coffee_price")
        if coffee_price:
            cafe.coffee_price = coffee_price
            db.session.commit()
            return jsonify({
                "success": "Successfully updated the price."
            })
        else:
            return jsonify({
                "error": {
                    "Not Found": "Sorry a cafe with that id was not found in the database."
                }
            })

# HTTP DELETE - Delete Record


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if request.method == "DELETE":
        if cafe:
            apiKey = request.args.get("api-Key")
            if apiKey == "TopSecretAPIKey":
                db.session.delete(cafe)
                db.session.commit()
                return jsonify({
                    "success": "Successfully deleted the cafe."
                })
            else:
                return jsonify({
                    "error": {
                        "Unauthorized": "Sorry, you are not authorized to delete this cafe."
                    }
                })
        else:
            return jsonify({
                "error": {
                    "Not Found": "Sorry a cafe with that id was not found in the database."
                }
            })


if __name__ == '__main__':
    app.run(debug=True)
