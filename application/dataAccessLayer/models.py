from application import db


class UserTable(db.Model):
    user_session_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    favorite_ingredient = db.Column(db.String(80), nullable=False)
    ingredients = db.relationship('IngredientsAnalysisTable', backref='user', lazy=True)

    def __repr__(self):
        return f'Author name:{self.name} email:{self.email} favorite_ingredient:{self.favorite_ingredient}'


class IngredientsAnalysisTable(db.Model):
    user_session_id = db.Column(db.Integer, db.ForeignKey('UserTable.user_session_id'), nullable=False)
    JSON_results = db.Column(db.LargeBinary)
    ingredients_analysis_id = db.Column(db.Integer, primary_key=True)
    meals = db.relationship('MealsAnalysisTable', backref='ingredients', lazy=True)

    def __repr__(self):
        return f'Author JSON_results:{self.JSON_results} ingredients_analysis_id: {self.ingredients_analysis_id}'


class MealsAnalysisTable(db.Model):
    ingredients_analysis_id = db.Column(db.Integer, db.ForeignKey('IngredientsAnalysisTable.ingredients_analysis_id'),
                                        nullable=False)
    crawled_meals = db.Column(db.LargeBinary)

    def __repr__(self):
        return f'Author crawled_meals:{self.crawled_meals}'



if __name__ == '__main__':
    db.create_all()
    db.session.commit()
