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

    # get form data
    zone_name = request.args.get("city_zone")
    current_time = None
    city_name = None

    if zone_name:
        try:
            # fetch time for selected timezone
            current_time = arrow.now(tz=zone_name)

            # format timezone e.g. America/New_York -> New York
            edit_timezone = zone_name.split("/")[-1]
            city_name = edit_timezone.replace("_", " ")

        except Exception:
            flash("Button clicked. Select a valid timezone first.")
            return redirect(url_for("index"))

    return render_template(
        "index.html",
        zone_data=TIMEZONE_DATA,
        zone_name=zone_name,
        current_time=current_time,
        city=city_name,
    )


if __name__ == "__main__":
    app.run()
