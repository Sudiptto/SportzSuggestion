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
    print(generated_text)


# Weatherstack API access key
access_key = '91234ae12b43ace8043cc65157f076a3'



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

        
        #print(f"Humidity: {current['humidity']}%")
        #print(f"Rain: {'Yes' if current['precip'] > 0 else 'No'}")
        #print(f"Temperature: {current['temperature']}°C")

        humidity = current['humidity']
        temperature = current['temperature']
        percipitation = current['precip']

weather_data('Brooklyn')

print(humidity)
print(temperature)
print(percipitation)

print(f"Name one sport that you can play when the temperature is {temperature}, when the humidity is {humidity}% and when the percipitation is level is {percipitation}%")

user_inputs(f"Name one unique sport that you can play when the temperature is {temperature}, when the humidity is {humidity}% and when the percipitation is level is {percipitation}%")

