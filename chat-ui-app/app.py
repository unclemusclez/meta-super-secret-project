import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.json
    landmark_type_filter = data.get("landmarkTypeFilter")
    search_keywords = data.get("searchKeywords")
    
    # Example GPS coordinates
    latitude = 40.7128
    longitude = -74.0060
    
    # Use MCP server to query nearby places
    nearby_places = query_nearby_places(latitude, longitude, landmark_type_filter, search_keywords)
    
    response = {
        "gps_coordinates": f"Latitude={latitude}, Longitude={longitude}",
        "nearby_places": nearby_places
    }
    return jsonify(response)

def query_nearby_places(latitude, longitude, landmark_type_filter, search_keywords):
    inference_url = os.environ.get('INFERENCE_URL')
    api_key = os.environ.get('API_KEY')
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "inputs": [
            {
                "name": "user_query",
                "shape": [1],
                "data": [f"Find nearby {landmark_type_filter} at latitude {latitude} and longitude {longitude}"],
                "datatype": "BYTES"
            }
        ]
    }
    
    response = requests.post(inference_url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        # Process the result to extract nearby places
        return result
    else:
        return ["Failed to retrieve data"]

if __name__ == "__main__":
    app.run(debug=True)