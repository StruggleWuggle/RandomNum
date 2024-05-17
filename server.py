from flask import Flask, jsonify
import random
import requests


def get_weather(url):
    """
    Set up HTTP request framework
    """
    response = requests.get(url)
    if response.status_code == 200:
        try:
            json_data = response.json()
            return json_data
        except ValueError:
            return {'error': 'Invalid JSON'}
    else:
        return {'error': f'Request failed with status code {response.status_code}'}

def wind_direction_to_int(direction):
    """
    Convert string character of wind direction into an arbitrary value
    """
    out_int = 9
    if direction == "N":
        out_int = 1
    elif direction == "NE":
        out_int = 2
    elif direction == "E":
        out_int = 3
    elif direction == "SE":
        out_int = 4
    elif direction == "S":
        out_int = 5
    elif direction == "SW":
        out_int = 6
    elif direction == "W":
        out_int = 7
    elif direction == "NW":
        out_int = 8
    return out_int

app = Flask(__name__)
@app.route('/getRand', methods=['GET'])
def get_data():
    # HTTP Request weather data from government site
    weather_data = (get_weather("https://api.weather.gov/gridpoints/LWX/45,93/forecast/hourly"))

    # Get random num between 1-100 from entropy of current system
    num_weather_nodes = random.SystemRandom().randint(1, 100)

    generated_seed = 0
    for i in range(num_weather_nodes):
        num = random.SystemRandom().randint(0, 155)
        temp = int(weather_data["properties"]["periods"][num]["temperature"])
        wind_speed = int(weather_data["properties"]["periods"][num]["windSpeed"][-5:-4])
        wind_direction = int(wind_direction_to_int(weather_data["properties"]["periods"][num]["windDirection"]))

        # Accumulate randomness, mixing entropy randomness with weather randomness
        generated_seed += ((temp + wind_speed*10 + wind_direction*100) * (i+1) * random.SystemRandom().randint(1, 10000))

    # Set random number generator seed as the generated seed
    random.seed(generated_seed)
    data = {
        'RandomNum': random.random(),
        'Seed': generated_seed
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=False)
