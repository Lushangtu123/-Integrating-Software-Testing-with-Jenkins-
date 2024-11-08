import pytest
from weather_station import collect_data, store_data, retrieve_data, analyze_data

def test_collect_data():
    """Test that data collection returns values within expected ranges."""
    data = collect_data()
    assert 15 <= data['temperature'] <= 30
    assert 30 <= data['humidity'] <= 70
    assert 950 <= data['pressure'] <= 1050

def test_store_data():
    """Test storing data in the database."""
    data = {'temperature': 25.5, 'humidity': 50.0, 'pressure': 1000.0}
    store_data(data)
    results = retrieve_data()
    assert len(results) > 0  # Check that data has been inserted

def test_retrieve_data():
    """Test retrieving data from the database."""
    results = retrieve_data()
    assert isinstance(results, list)  # Ensure it returns a list
    if results:  # If there is data, check structure
        assert len(results[0]) == 5  # (id, timestamp, temperature, humidity, pressure)

def test_analyze_data():
    """Test data analysis function, e.g., average temperature calculation."""
    results = retrieve_data()
    if results:  # Only test if there is data available
        analysis = analyze_data()
        assert 'average_temperature' in analysis
        assert isinstance(analysis['average_temperature'], (float, type(None)))

# Run tests with pytest in terminal:
# pytest --junitxml=report.xml
