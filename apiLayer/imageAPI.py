from flask import Flask, render_template, request, redirect, url_for
from servicesLayer.aiApiCallService import classification
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
        uploaded_file = request.files['filepip freeze > requirements.txt']
        print(uploaded_file)
        ingredients_detection = classification(uploaded_file)
        return {
            'data': ingredients_detection
        }

    else:
        return 'backend works good'

if __name__ == "__main__":
    app.run(debug=True)



#2 comandos:

#export FLASK_APP=imageAPI.py

#opcion para q cuando se haga algun cambio se actualice por si solo: export FLASK_DEBUG=1

#flask run