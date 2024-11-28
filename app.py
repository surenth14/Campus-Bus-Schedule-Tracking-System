from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# Dummy bus times data (static example)
bus_times = {
    "Station A": ["08:30", "09:00", "09:30", "10:00"],
    "Station B": ["08:45", "09:15", "09:45", "10:15"]
}

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Bus time prediction route (API)
@app.route('/predict', methods=['POST'])
def predict():
    start_station = request.form['start_station']
    destination_station = request.form['destination_station']
    
    # Example logic: Get bus times for the start station (you can replace this with prediction logic)
    if start_station in bus_times:
        times = bus_times[start_station]
        return jsonify(times)
    else:
        return jsonify({"error": "Station not found!"})

if __name__ == '__main__':
    app.run(debug=True)
