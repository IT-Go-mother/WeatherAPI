import requests

try:
    api_key = '99c09094c562cfb110c16e7fcbeb4d5e'

    city = "O"
    sum = 0
    count = 0
    while city != "Q":
        city = input("*Q* - exit\nPlease city: ")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            sum += temperature
            count += 1
            print(f"Temperature: {temperature}°C")
        else:
            print("City isnt found.")

    average = sum / count
    print(f"Average Temperature: {average}°C")

except:
    print("ERROR!")
