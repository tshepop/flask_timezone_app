import csv
from flask import Flask, request, render_template, redirect, url_for, flash
import arrow
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY


def create_timezone_list(filepath="time_zone.csv"):
    """Get timezones from a csv file, store and return list."""

    zones = []

    try:
        # get data from a file
        with open(filepath, "r") as f:
            reader = csv.reader(f)
            next(reader, None)

        for row in reader:
            if row:
                zones.append(row[0].strip())
    except FileNotFoundError:
        print(f"{filepath} not found. Check correct path.")

    return zones


# load timezones into memory, to reduce server resources
TIMEZONE_DATA = create_timezone_list()


@app.route("/", methods=["GET", "POST"])
def index():
    zone_data = create_timezone_list()

    # get form data
    zone_name = request.form.get("city_zone")
    current_time = arrow.now(tz=zone_name)

    if request.method == "POST":
        if not zone_name or not current_time:
            flash("Make a Valid Selection!")
            redirect(url_for("index"))

    # create a list and extract city name
    city = str(zone_name).split("/")

    return render_template(
        "index.html",
        current_time=current_time,
        zone_data=zone_data,
        zone_name=zone_name,
        city=city,
    )


if __name__ == "__main__":
    app.run()
