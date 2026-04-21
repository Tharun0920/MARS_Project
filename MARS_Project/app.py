from flask import Flask, jsonify, request
from risk_synthesis import calculate_node_risk

app = Flask(__name__)

# 1. The Home Route (To check if the server is running)
@app.route('/')
def home():
    return jsonify({
        "project": "M.A.R.S. Engine",
        "status": "Operational",
        "message": "Multi-domain Anomaly & Risk Synthesis Engine is Online"
    })

# 2. The Risk Assessment Route
@app.route('/get_risk', methods=['GET'])
def get_risk():
    # Get parameters from the URL (e.g., /get_risk?lat=13.5&lon=79.2)
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    # For now, we simulate finding the scores in our CSVs 
    # (We will build the actual search logic in Week 3)
    dummy_army_score = 0.5
    dummy_navy_score = 0.2
    dummy_isro_score = 0.1
    
    # Use our Day 5 logic to calculate the risk
    total_risk = calculate_node_risk(dummy_army_score, dummy_navy_score, dummy_isro_score)
    
    return jsonify({
        "location": {"latitude": lat, "longitude": lon},
        "risk_score": total_risk,
        "status": "Success"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)