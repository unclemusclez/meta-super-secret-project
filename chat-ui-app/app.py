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
    
    # Here you can add logic to process the filter and search keywords
    # and generate a response based on the Google Maps tool calls
    response = f"Response to: Filter={landmark_type_filter}, Search={search_keywords}"
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)