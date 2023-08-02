import requests

def get_weather_data():

    url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&dt=1690880642&APPID={your api key}'
    
    api_key = 'your api key' if 'your api key' else None
    
    try:
        response = requests.get(url, params={'apikey': api_key})
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error while fetching weather data:", e)
        return None

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            weather_data = get_weather_data()
            if weather_data:
                print("Current weather:", weather_data.get('weather'))
            else:
                print("Failed to fetch weather data.")
        elif choice == '2':
            weather_data = get_weather_data()
            if weather_data:
                print("Wind Speed:", weather_data.get('wind'))
            else:
                print("Failed to fetch weather data.")
        elif choice == '3':
            weather_data = get_weather_data()
            if weather_data:
                print("Pressure:", weather_data.get('main', {}).get('pressure'))
            else:
                print("Failed to fetch weather data.")
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
