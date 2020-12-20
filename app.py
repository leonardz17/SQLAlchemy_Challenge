from flask import Flask, jsonify

import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Database setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
measurement = Base.classes.measurement
station = Base.classes.station

# Create app
app = Flask(__name__)

# Define routes
@app.route("/")
def home():
    print("Received request for Home page")
    return(
        f"Welcome to the Climate App! <br/>"
        f"Available Routes: <br/>"
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/<start><br/>'
        f'/api/v1.0/<start>/<end><br/>'
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create session
    session = Session(engine)
    # Query measurement table for date and prcp
    results = session.query(measurement.date, measurement.prcp).all()
    session.close()

    # Create a dictionary
    prcp_dict = {
        date: prcp for date, prcp in results
    }
    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def stations():
    # Create session
    session = Session(engine)
    # Query measurement table for date and prcp
    results = session.query(station.station).all()
    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)
@app.route("/api/v1.0/tobs")
def tobs():
    # Create session
    session = Session(engine)
    # Query measurement table for date and prcp
    results = session.query(station.station).all()
    session.close()

    oneyear_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    busiest_station = session.query(measurement.tobs).\
    filter(measurement.station == 'USC00519281', measurement.date >= oneyear_date).all()
    temp_values = list(np.ravel(busiest_station))

    return jsonify(temp_values)
@app.route("/api/v1.0/<start>")
def start_date(start):
    session = Session(engine)
    results = list(np.ravel(session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
                filter(measurement.date >= start).all()))
    session.close()
   
    all_dates = list(np.ravel(session.query(measurement.date).all()))
  
    for date in all_dates:
       if start == date:
           return jsonify(results) 
    return jsonify({"error": f"Date {start} not found."}), 404
    

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    session = Session(engine)
    results = list(np.ravel(session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
                filter(measurement.date >= start).\
                filter(measurement.date <= end).all()))
    session.close()

    all_dates = list(np.ravel(session.query(measurement.date).all()))
  
    for date in all_dates:
       if start == date:
           for date in all_dates:
               if end == date:
                    return jsonify(results) 
    return jsonify({"error": f"Date {start} and/or {end} not found."}), 404
   
    
if __name__ == '__main__':
    app.run(debug=True)