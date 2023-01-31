import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def myapp():
    url = "https://www.w3schools.com/"
    response = requests.get(url)

    print(response)
    return render_template("index.html", res = response.status_code)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
