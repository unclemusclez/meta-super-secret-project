import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/narrative-content", methods=["GET"])
def narrative_content():
    # Example narrative content
    narrative = "This is an example narrative content about nearby landmarks."
    return jsonify({"narrative": narrative})

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
    inference_url = os.environ.get('API_ENDPOINT_TOOL_CALLS')
    api_key = os.environ.get('API_KEY_TOOL_CALLS')
    model = os.environ.get('MODEL_TOOL_CALLS')
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": f"Find nearby {landmark_type_filter} at latitude {latitude} and longitude {longitude}"
            }
        ]
    }
    
    response = requests.post(inference_url, headers=headers, json=data)
    print(f"API call status code: {response.status_code}")
    print(f"API call response: {response.text}")
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return ["Failed to retrieve data"]

if __name__ == "__main__":
    app.run(debug=True)