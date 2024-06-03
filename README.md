# Flask Timezone Web App

The web app that uses backend and frontend technology to display time zones. The aim of the website or web app is to use timezones as input, from the response extract date, time and the city name. The timezone data is from a csv file created from [TimeZoneDB](https://timezonedb.com/download) the csv file has been narrowed to a few timezones.

The website is created with Python3, flask, bootstrap5, arrow package. The html select is populated with timezones. After choosing and formatted details are displayed.

## Installation

To install packages and run the website in your local device(laptop, desktop)

- Create a virtual environment

```$ python3 -m venv venv```

- Activate the virtual environment

```$ source venv\bin\activate```

- Install required packages

```$ python3 install -r requirements.txt```

- Start local server

```$ flask run```

   or

```$ python3 -m flask --app [name of app] run```


