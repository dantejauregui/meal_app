from flask import Flask, request
from application.servicesLayer.aiApiCallService import classification
from pprint import pprint

from application import app
from application.dataAccessLayer.models import UserTable, MealsAnalysisTable
from application import db
from application.servicesLayer.crawlerService import get_web


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


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        response = request.json
        form_username = response['Name']
        form_email_name = response['Email']
        form_ingredient_name = response['FavoriteIngredient']

        # Inserting records in DB
        user = UserTable(name=form_username, email=form_email_name, favorite_ingredient=form_ingredient_name)
        db.session.add(user)
        db.session.commit()

        generated_meal_ideas = get_web(form_ingredient_name)

        # 3. map, structure the data and store in DB in imageAPI.py ...
        for i in generated_meal_ideas:
            meals = MealsAnalysisTable(suggested_meal_title=i[0], suggested_meal_url=i[1])
            db.session.add(meals)
            db.session.commit()

        # 4. trying to send the filtered data from my DB to UI:
        filtered_meals = MealsAnalysisTable.query.order_by(MealsAnalysisTable.meal_suggestion_id.desc()).limit(5).all()
        serialize_meals = MealsAnalysisTable.serialize_list(filtered_meals)

        #using prettyprint:
        pprint(serialize_meals)

        return {
            'data': serialize_meals
        }
    else:
        return 'FORM backend works good'



