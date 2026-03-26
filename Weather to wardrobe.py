import math
import json
import os
from statistics import mode

def calculate_feels_like(temp, humidity):
    # If there is cold, humidity matters less. If it's hot, it's a 'steamer'.
    if temp > 26:
        return temp + (0.55 * (temp - 14.5) * (humidity / 100))
    return temp

DATA_FILE = "commute_log.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    # Initial Seed Data: [Temp, Humidity, Wind, Wardrobe]
    return [
        [30, 80, 5, "Light Cotton"],
        [20, 40, 15, "Full Sleeves"],
        [10, 20, 20, "Heavy Jacket"],
        [25, 90, 2, "Light Cotton"]
    ]

def suggest_wardrobe(current_weather, history, k=3):
    distances = []
    curr_temp, curr_hum, curr_wind = current_weather
    curr_feels = calculate_feels_like(curr_temp, curr_hum)

    for entry in history:
        hist_temp, hist_hum, hist_wind, outfit = entry
        hist_feels = calculate_feels_like(hist_temp, hist_hum)
        
        dist = math.sqrt(
            (curr_feels - hist_feels)**2 + 
            (curr_wind - hist_wind)**2
        )
        distances.append((dist, outfit))

    distances.sort(key=lambda x: x[0])
    neighbors = [d[1] for d in distances[:k]]
    
    return mode(neighbors)

history = load_data()

print("---Weather-to-Wardrobe Advisor ---")
t = float(input("Enter Morning Temp (°C): "))
h = float(input("Enter Humidity (%): "))
w = float(input("Enter Wind Speed (km/h): "))

today = [t, h, w]
recommendation = suggest_wardrobe(today, history)

print(f"\nBased on your history, you should wear: **{recommendation}**")

feedback = input("\nWas this suggestion comfortable? (yes/no): ").lower()
if feedback == "no":
    correct_outfit = input("What should you have worn? ")
    history.append([t, h, w, correct_outfit])
    with open(DATA_FILE, 'w') as f:
        json.dump(history, f)
    print("Logged! I'll remember that for next time.")
else:
    print("Great! Stay comfortable out there.")
