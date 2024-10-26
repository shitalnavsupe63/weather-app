from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    return response.json()

    

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city_name = request.form['city']
        api_key = "ff730c845c85ecd214ccd8113e5ab081"
        weather_data = get_weather(city_name, api_key)
    
    return render_template('index.html', weather_data = weather_data)


if __name__ == "__main__":
    app.run(debug=True)
