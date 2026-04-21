import pandas as pd
import random
from datetime import datetime, timedelta

# 1. Define the parameters for our synthetic data
NUM_REPORTS = 500  # We will generate 500 fake field reports

# Phrases that indicate low or no threat
benign_phrases = [
    "Routine patrol completed with no incidents.",
    "Supply convoy arrived safely at checkpoint.",
    "Weather clear, visibility good. No movement detected.",
    "Civilian traffic normal along the main highway.",
    "Radio equipment maintenance finished."
]

# Phrases that indicate a high threat or anomaly
threat_phrases = [
    "Unidentified armed personnel spotted near the perimeter.",
    "Suspected IED wires visible on the dirt road.",
    "Small arms fire heard 2 kilometers North.",
    "Unauthorized drone observed hovering over the base.",
    "Vehicle abandoned near the bridge, investigating for explosives."
]

data = []
start_date = datetime.now() - timedelta(days=30) # Data from the last 30 days

# 2. Loop to generate the data
for i in range(NUM_REPORTS):
    report_id = f"RPT-{1000 + i}"
    timestamp = start_date + timedelta(hours=random.randint(1, 720))
    
    # Generate random GPS coordinates (roughly simulating a region)
    # Latitude between 12.0 and 15.0, Longitude between 77.0 and 80.0
    lat = round(random.uniform(12.0, 15.0), 4)
    lon = round(random.uniform(77.0, 80.0), 4)
    
    # Randomly decide if this report is a threat or benign (30% chance of threat)
    is_threat = random.random() < 0.3
    
    if is_threat:
        text_report = random.choice(threat_phrases)
        actual_threat_score = round(random.uniform(0.7, 1.0), 2) # High risk
    else:
        text_report = random.choice(benign_phrases)
        actual_threat_score = round(random.uniform(0.0, 0.3), 2) # Low risk
        
    data.append([report_id, timestamp, lat, lon, text_report, actual_threat_score])

# 3. Create a Pandas DataFrame and save it as a CSV
df = pd.DataFrame(data, columns=['Report_ID', 'Timestamp', 'Latitude', 'Longitude', 'Raw_Text', 'Actual_Threat_Score'])

# Save to the data folder
file_path = 'data/army_intel_data.csv'
df.to_csv(file_path, index=False)

print(f"Success! {NUM_REPORTS} synthetic Army field reports generated and saved to {file_path}")