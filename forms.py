from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, NumberRange, Length



class AddNewPet(FlaskForm):
    name = StringField("Pet Name", validators=[
                       InputRequired(message="Pet Name can't be blank")])
    species = SelectField("Species", choices=[
                       ("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available", validators=[
                        InputRequired(message="Must be available if added")])
class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional()])

    notes = TextAreaField(
        "Notes",
        validators=[Optional(), Length(min=10)])

    available = BooleanField("Available?")