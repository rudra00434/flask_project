from flask import Flask, request, jsonify, render_template, send_from_directory,redirect,url_for
import folium
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save_location', methods=['POST'])
def save_location():
    data = request.get_json()
    lat = data['latitude']
    lon = data['longitude']

    print(f"[INFO] Received coordinates: {lat}, {lon}")

    # Create map
    my_map = folium.Map(location=[lat, lon], zoom_start=16)
    folium.Marker([lat, lon], popup="You are here").add_to(my_map)

    # Save to static folder
    map_path = os.path.join("static", "user_location.html")
    my_map.save(map_path)

    return jsonify({"message": "✅ Location received. Opening map..."})

@app.route('/map')
def show_map():
    lat=request.args.get('lat')
    lon=request.args.get('lon')
    return render_template('user_location',lat=22.57,lon=88.36)

if __name__ == '__main__':
    app.run(debug=True)