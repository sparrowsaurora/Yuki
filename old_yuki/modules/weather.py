# https://open-meteo.com/en/docs#hourly=&daily=
import requests, speech_output


# Function to get the weather from Open-Meteo
def get_weather(lat, lon):
    """
    Fetches the current weather and daily forecast data for the given latitude and longitude using Open-Meteo.
    - lat: Latitude of the location.
    - lon: Longitude of the location.

    Returns a dictionary with the weather details.
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&daily=temperature_2m_max,uv_index_max,precipitation_probability_mean&timezone=Australia/Perth"
    
    try:
        # Make a request to Open-Meteo
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()  # Parse JSON response
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

# Main function
def main():
    # Coordinates for Mahogany Creek, Western Australia
    latitude = -31.8976
    longitude = 116.1124

    # Get the current weather data
    weather_data = get_weather(latitude, longitude)

    # Display the weather data
    if weather_data:
        # Print raw data for debugging purposes
        # print("Raw weather data:", weather_data)

        # Extract current weather data
        current_weather = weather_data.get("current_weather", {})
        temperature = current_weather.get("temperature", "N/A")


        # Extract daily forecast data
        daily_forecast = weather_data.get("daily", {})
        max_temp = daily_forecast.get("temperature_2m_max", ["N/A"])[0]
        uv_index_max = daily_forecast.get("uv_index_max", ["N/A"])[0]
        chance_of_rain = daily_forecast.get("precipitation_probability_mean", ["N/A"])[0]

        # Print the weather information
        speech_output.speak(f"Current Weather in Mahogany Creek, WA:")
        speech_output.speak(f"Current Temperature: {temperature}°C")

        speech_output.speak(f"Max Temperature Today: {max_temp}°C")
        speech_output.speak(f"UV Index Max Today: {uv_index_max}")
        speech_output.speak(f"Chance of Rain Today: {chance_of_rain}%")
    else:
        speech_output.speak("No weather data to display.")

main()
