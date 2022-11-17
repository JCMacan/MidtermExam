from flask import Flask, jsonify, request

app = Flask(__name__)
heart=[
    {
        "Heart_id": "01",
        "Date": "November 17, 2022",
        "Heart_rate": "100 bpm" 

    },
    {
        "Heart_id": "02",
        "Date": "November 17, 2022",
        "Heart_rate": "125  bpm"
    },
    {
        "Heart_id": "03",
        "Date": "November 17, 2022",
        "Heart_rate": "155 bpm"
    }
]

@app.route('/heart', methods=['GET'])
def displayHeart():
    return jsonify(heart)


@app.route('/heart', methods=['POST'])
def addHeart():
    heart1 = request.get_json()
    heart.append(heart)
    return {'id': len(heart)},200

@app.route('/heart/<int:index>', methods=['DELETE'])
def deleteheart(index):
    heart.pop(index)
    return 'Heart rate ID was successfully deleted',200

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)