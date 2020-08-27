from flask import Flask, request, render_template, redirect, flash, url_for, jsonify
import json
import os
import requests
import math

weather_key = str(os.environ["WEATHER_KEY"])

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/weather")
def main_page():
    return render_template("weather.html")

@app.route("/weather", methods = ["POST"])
def get_weather():
    if request.form["zip"] == "":
        flash("Error: ZIP code is required!")
        return render_template("weather.html")
    
    zip_code = request.form["zip"]
    

    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid="+weather_key)
    y = r.json()

    temp = ""

    area_name = y["name"]

    if request.form["temptype"] == "fahrenheit":
        temp = (y["main"]["temp"] - 273.15) * 9/5 + 32.0
    else:
        temp = y["main"]["temp"] - 273.15

    return render_template("searched_weather.html", output=round(temp), selected=request.form["temptype"], zip=zip_code, area=area_name)