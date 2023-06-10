from flask import Flask, render_template, flash, redirect, request, url_for, jsonify, session
from tester import * # import everything from the tester.py folder 
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_PASSWORD')


#lat = None


@app.route('/info', methods=['POST'])
def info():
    if request.method == 'POST':
        req = request.get_json()
        #print(req)
        # create a global lat variable to be used
        #global lat
        lat = req['lat']
        print(lat)

        worked = "It worked!"

    # Return the worked variable as a JSON response

    # NOTE FOR TOMORROW OR LATER TODAY THE WORKED SENT!
        return jsonify({'worked': worked})
    

    #return render_template('home.html', lat=None)


@app.route('/', methods=['GET', 'POST'])
def home():
    #global lat
    if request.method == 'POST':
        city = request.form['city']
        # Process the city data as needed
        #print(type(city))
        # weather_info is a list of weather info
        weather_info = weather_data(city)
        # returning a list of information 
        if 'None' in weather_info:
            flash('Not a valid city', 'success')
            return redirect(url_for('home'))
        elif len(weather_info) == 5:
            humidity = weather_info[0]
            temperature = weather_info[1]
            percipitation = weather_info[2]
            cloud_cover = weather_info[3]
            wind_speed = weather_info[4]

            # After this use the OpenAI api, feed the weather data above to the API and then flash the final result
            ai_suggestion = user_inputs(f"Name one unique sport that you can play when the temperature is {temperature}, when the humidity is {humidity}% and when the percipitation is level is {percipitation}% and when the percentage of clouds in the sky is {cloud_cover} and finally when the wind speed is {wind_speed} miles per hour")

            print(ai_suggestion)

            flash(f'The sport best fit: {ai_suggestion}', 'success')
            return redirect(url_for('home'))
        
        

        # If the user pressed the other button

            
    

    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)