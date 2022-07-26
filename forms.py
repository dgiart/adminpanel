from wtforms import Form,  StringField, TextAreaField



class CitizenForm(Form):
    fio = StringField('ФИО')
    phone = StringField('Телефон')
    birth = StringField('Дата рождения')