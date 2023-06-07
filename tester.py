import openai
import requests
from password import *
# Set up your OpenAI API credentials
openai.api_key = api_key

# Prompt the user for input

def user_inputs(user_prompt):
    # Generate text using the OpenAI API
    response = openai.Completion.create(
        engine='text-davinci-003',  # Specify the model to use
        prompt=user_prompt,
        n=1,  # Limit to a single completion
        max_tokens=5,  # Specify the maximum length of the generated text
    )

    # Get the generated text from the API response
    generated_text = response.choices[0].text.strip()

    # Print the generated text
    return generated_text

def weather_data(city):
    # Make the API request
    url = f"http://api.weatherstack.com/current?access_key={access_key}&query={city}"
    response = requests.get(url)
    data = response.json()
    # Check if the API request was successful
    if 'success' in data and not data['success']:
        print(f"Error: {data['error']['info']}")
    else:
        # Extract and display weather information
        current = data['current']

        global humidity
        global temperature
        global percipitation
        #global type_precip
        global cloud_cover
        global wind_speed

        humidity = current['humidity']
        temperature = current['temperature']
        percipitation = current['precip']
        #type_precip = current['precip_type'] - may not work for certain cities
        cloud_cover = current['cloudcover']
        wind_speed = current['wind_speed']
        
        return [humidity, temperature, percipitation, cloud_cover, wind_speed]


        # Note for future, instead of saving these variables i made it a list so i can reutnr it to the mapp.py file and this will make organization much easier as I dont have to put this code on mapp.py
"""""""""
#weather_data('Brooklyn')

print(humidity)
print(temperature)
print(percipitation)
#print(type_precip)
print(cloud_cover)
print(wind_speed)

"""""
"""""""""

print(f"Name one sport that you can play when the temperature is {temperature}, when the humidity is {humidity}% and when the percipitation is level is {percipitation}% and the type of percipitation is {type_precip} and finally when the percentage of clouds in the sky is {cloud_cover}")

user_inputs(f"Name one sport that you can play when the temperature is {temperature}, when the humidity is {humidity}% and when the percipitation is level is {percipitation}% and the type of percipitation is {type_precip} and finally when the percentage of clouds in the sky is {cloud_cover}")

"""""
# ----- This works returns the correct variable
#print(f"Name one sport that you can play when the temperature is {temperature}, when the humidity is {humidity}% and when the percipitation is level is {percipitation}% and finally when the percentage of clouds in the sky is {cloud_cover}")

#user_inputs(f"Name one sport that you can play when the temperature is {temperature}, when the humidity is {humidity}% and when the percipitation is level is {percipitation}% and when the percentage of clouds in the sky is {cloud_cover} and finally when the wind speed is {wind_speed} miles per hour")