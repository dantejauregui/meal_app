from flask import Flask, request
from application.servicesLayer.aiApiCallService import classification
from flask_cors import CORS

from application import app
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

#@app.route('/form', methods=['POST'])
#def form():
 # receive data from UI FORM: name, email and favoriteIngredient
 # so: 1.store data with sql alchemy
 # 2.execute crawlerService.py
 # 3. map, structure the data and store in DB in imageAPI.py
 # 4.return ideas of meals to UI as JSON


#if __name__ == "__main__":
#    app.run(debug=True)
