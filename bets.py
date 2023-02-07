import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Make a request to the-odds-api with your API key
    url = "https://api.the-odds-api.com/v3/sports?apiKey=97ab2a4c0406183c48d997e2ad02f2e9"
    response = requests.get(url)
    data = response.json()
    
    # Extract the list of sports from the response
    sports = data['data']
    
    # Render the HTML template and pass the list of sports to it
    return render_template('index.html', sports=sports)

if __name__ == '__main__':
    app.run(debug=True)