from application import db


class UserTable(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    user_session_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    favorite_ingredient = db.Column(db.String(80), nullable=False)
    ingredients = db.relationship('MealsAnalysisTable', backref='user', lazy=True)

    def __repr__(self):
        return f'Author name:{self.name} email:{self.email} favorite_ingredient:{self.favorite_ingredient}'

class MealsAnalysisTable(db.Model):
    __tablename__ = 'meals'
    __table_args__ = {'extend_existing': True}
    meal_suggestion_id = db.Column(db.Integer, primary_key=True)
    user_session_id = db.Column(db.Integer, db.ForeignKey('users.user_session_id'), nullable=True)
    suggested_meal_title = db.Column(db.String(300), nullable=False)
    suggested_meal_url = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'Author suggested_meal_title:{self.suggested_meal_title} suggested_meal_url:{self.suggested_meal_url}'

# Activate this code in order to create the Database:
#if __name__ == '__main__':
#    db.create_all()
#    db.session.commit()