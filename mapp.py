from flask import Flask, render_template, request, flash
from tester import * # import everything from the tester.py folder 
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        # Process the city data as needed
        print(type(city))
        
        x = weather_data(city)
        print(x)
        """""""""
        # printing from the tester.py folder
        #print(humidity)
        print(temperature)
        print(percipitation)
        print(cloud_cover)
        print(wind_speed)
        """""
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)