#Importing dependencies
import numpy as np
import pandas as pd
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify

#Setup the Database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
Base.classes.keys()
# reflect the tables
Base.prepare(engine, reflect = True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)
inspector = inspect(engine)


#Creating the app
app = Flask(__name__)

#Define the routes
@app.route("/")
def home():
    return(
            f"Welcome to my page where I display the information for my Climate Starter file"
            f"<br/>"
            f"<br/>"
            f"The following routes are available to visit"
            f"<br/>"
            f"/api/v1.0/precipitation<br/>"
            f"/api/v1.0/stations<br/>"
            f"/api/v1.0/tobs<br/>"
            f"/api/v1.0/start<br/>"
            f"/api/v1.0/start/end<br/>"
            )

@app.route("/api/v1.0/precipitation")
#Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.
#Return the JSON representation of your dictionary.

def precipitation():
    latest_date_precip = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    # Calculate the date 1 year ago from the last data point in the database
    a_year_ago = dt.date(2017,8,23) - dt.timedelta(days = 365)

    # Perform a query to retrieve the date and precipitation scores
    precip_scores = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > a_year_ago).order_by(Measurement.date).all()

    #create a dict with 'date' and 'prcp' as the keys and values
    rain_total = []
    for result in precip_scores:
        row={}
        row["date"] = precip_scores[0]
        row["prcp"] = precip_scores[1]
        rain_total.append(row)
    
    return jsonify(rain_total)

@app.route("/api/v1.0/stations")
#Return a JSON list of stations from the dataset.

def stations():
# Design a query to show how many stations are available in this dataset?
    stations = session.query(Station.station).all()
    station_list= list(np.ravel(stations))
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
#query for the dates and temperature observations from a year from the last data point.
#Return a JSON list of Temperature Observations (tobs) for the previous year.

def temperature():
    latest_date_precip = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    # Calculate the date 1 year ago from the last data point in the database
    a_year_ago = dt.date(2017,8,23) - dt.timedelta(days = 365)

    # Perform a query to retrieve the date and temperature scores
    temp_scores = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > a_year_ago).order_by(Measurement.date).all()

    #create a dict with 'date' and 'tobs' as the keys and values
    temp_total = []
    for result in temp_scores:
        row={}
        row["date"] = temp_scores[0]
        row["prcp"] = temp_scores[1]
        temp_total.append(row)
    
    return jsonify(temp_total)

@app.route("/api/v1.0/start")
#Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
#When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.


def start():
    start_date= dt.datetime(2011,10,3)
    last_year = dt.timedelta(days=365)
    start = start_date-last_year
    start_trip_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)). filter(Measurement.date >= start).all()
    trip = list(np.ravel(start_trip_data))
    return jsonify(trip)

@app.route("/api/v1.0/start/end")

def start_end():
  # go back one year from start/end date and get Min/Avg/Max temp     
    start_date= dt.datetime(2011,10,3)
    end_date= dt.datetime(2011,10,23)
    last_year = dt.timedelta(days=365)
    start = start_date-last_year
    end = end_date-last_year
    between_trip_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)). filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    trip = list(np.ravel(between_trip_data))
    return jsonify(trip)

if __name__ == "__main__":
    app.run(debug=True)
