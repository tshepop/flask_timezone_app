import csv
from flask import Flask, request, render_template, redirect, url_for, flash
import arrow

app = Flask(__name__)


def create_timezone_list():
    """Get timezones from a csv file, store and return list."""

    zones = []

    # get data from a file
    with open("time_zone.csv") as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for idx, row in enumerate(header_row):
            pass
        #   print(idx, row)

        for row in reader:
            zones.append(row[0])

    return zones


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
    city = zone_name.split("/")

    return render_template("index.html",
                           current_time=current_time,
                           zone_data=zone_data,
                           zone_name=zone_name,
                           city=city)


if __name__ == "__main__":
    app.run()
