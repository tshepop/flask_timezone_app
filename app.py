import csv
from flask import Flask, request, render_template
import arrow

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    zones = []

    # get data from csv file
    with open("time_zone.csv") as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for idx, row in enumerate(header_row):
            # print(idx, row)
            pass

        for row in reader:
            zones.append(row[0])

    # get form data
    if request.method == "POST":
        get_selected_zone = request.form.get("city_zone")

    # Context - dictionary to populate the form select element
    # and pass the data to the template
    data = {
        "zones": zones,
        "name_zone": get_selected_zone,
    }

    # use the arrow package to get date and time
    current_time = arrow.now(tz=get_selected_zone)

    return render_template("index.html",
                           current_time=current_time,
                           data=data)


if __name__ == "__main__":
    app.run()
