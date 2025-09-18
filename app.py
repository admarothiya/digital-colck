from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time')
def time_endpoint():
    now = datetime.now()
    return jsonify(
        time=now.strftime('%I:%M:%S %p'),
        date=now.strftime('%d-%m-%Y')
    )

if __name__ == '__main__':
    app.run(debug=True)
