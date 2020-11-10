from flask import Flask, request
from application.servicesLayer.aiApiCallService import classification
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        print(uploaded_file)
        ingredients_detection = classification(uploaded_file)
        return {
            'data': ingredients_detection
        }

    else:
        return 'backend works good'


if __name__ == "__main__":
    app.run(debug=True)
