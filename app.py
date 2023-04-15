from flask import Flask, request, jsonify, render_template
from logic import analyze_birthday

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def analyze_data():
    # POST 요청으로부터 데이터 가져오기
    data = request.get_json()


    print(data)
    return analyze_birthday(data["birthday1"], data["gender1"], data["birthday2"], data["gender2"], data["question"])


if __name__ == '__main__':
    app.run(debug=True)


