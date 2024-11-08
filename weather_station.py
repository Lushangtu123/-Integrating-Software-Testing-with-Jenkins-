import random
import sqlite3
from datetime import datetime

# Database setup
conn = sqlite3.connect('weather_data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS WeatherData (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        temperature REAL,
        humidity REAL,
        pressure REAL
    )
''')
conn.commit()

def collect_data():
    """Simulate data collection from sensors."""
    return {
        'temperature': round(random.uniform(15, 30), 2),
        'humidity': round(random.uniform(30, 70), 2),
        'pressure': round(random.uniform(950, 1050), 2)
    }

def store_data(data):
    """Store collected data in the database."""
    timestamp = datetime.now().isoformat()
    cursor.execute('''
        INSERT INTO WeatherData (timestamp, temperature, humidity, pressure)
        VALUES (?, ?, ?, ?)
    ''', (timestamp, data['temperature'], data['humidity'], data['pressure']))
    conn.commit()

def retrieve_data():
    """Retrieve all weather data entries from the database."""
    cursor.execute('SELECT * FROM WeatherData')
    return cursor.fetchall()

def analyze_data():
    """Analyze data trends (e.g., calculate average temperature)."""
    cursor.execute('SELECT AVG(temperature) FROM WeatherData')
    avg_temp = cursor.fetchone()[0]
    return {'average_temperature': avg_temp}

def display_data():
    """Display stored data and analysis results."""
    data = retrieve_data()
    analysis = analyze_data()
    print("Weather Data Records:")
    for entry in data:
        print(f"Timestamp: {entry[1]}, Temp: {entry[2]}, Humidity: {entry[3]}, Pressure: {entry[4]}")
    print("\nAnalysis Results:")
    print(f"Average Temperature: {analysis['average_temperature']}°C")

# Example execution
if __name__ == '__main__':
    data = collect_data()
    store_data(data)
    display_data()
