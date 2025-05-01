from flask import Flask, render_template, request
import requests
import config

app = Flask(__name__)

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"]
        }
        return weather_data
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        weather = get_weather(city)
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
