from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class CitynameSearchForm(FlaskForm):
    town = StringField('Nazwa miasta', validators=[DataRequired()])
    submit = SubmitField('Szukaj')
    
    
class PostcodeSearchForm(FlaskForm):
    code = StringField('Kod pocztowy', validators=[DataRequired(), Length(min=6, max=6, message="Nie poprawny zapis!")])
    submit = SubmitField('Szukaj')