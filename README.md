# SQLAlchemy_Challenge

## Table of Contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Main Files](#main-files)
* [Analysis](#analysis)

## Introduction
Analyze weather data from various weather stations in Hawaii to plan the perfect vacation. Using SQLAlchemy I queried through the data to see weather patterns for specified dates. Weather data was also jsonified and can be viewed through Flask. 

## Technologies
* SQLAlchemy 
* Flask
* Pandas
* Matplotlib
* JSON

## Main Files
* climate_analysis - main jupyter notebook containing all analysis 
* app.py - codes for flask API

## Analysis 
Looking at a one year range from the latest date we can see that the months with the heaviest rainfall totals is August, February, April, and July with an average of 0.177 inches of rain. Using the station with the most readings we can see that in that one year range, the temperature is consistently in the 70-80 degree range with around 75 degrees being the most common temperature. 