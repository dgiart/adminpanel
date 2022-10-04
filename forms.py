from wtforms import Form,  StringField, TextAreaField, validators, RadioField, SelectField, DateField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Length
from admin_data import districts

citizen_data = {'fio': '', 'phone': '', 'birth': '', 'addr': '', 'people_num': '', 'people_fio': '',
                             'invalids': '', 'children': '', 'children_age': '', 'food': '', 'drugs': '', 'water': '',
                             'products_detail': '', 'gigien': '', 'gigien_num': '', 'pampers': '', 'diet': '',
                             'pers_data_agreement': '', 'photo_agreement': ''}


class CitizenForm(Form):
    # fio = StringField('ФИО')
    family = StringField('Фамилия', validators=[InputRequired()])
    name = StringField('Имя')
    paternal = StringField('Отчество')
    phone = StringField('Телефон')
    birth = StringField('Дата рождения')
    # birth = DateField('Дата рождения?', format='%Y-%m-%d')
    # addr = StringField('Адресс')
    city = StringField('Город')
    distr = SelectField('Район', choices=districts)
    # distr = RadioField('Район', choices=[('value', 'Шевченковский'),('value_two', 'Киевский')])
    # distr = StringField('Район')
    street = StringField('Улица')
    house = StringField('Дом')
    apartment = StringField('Квартира')
    people_num = StringField('Число проживающих')
    people_fio = StringField('Фио проживающих')
    invalids = RadioField('Есть ли инвалиды', choices=['Да', 'Нет'])
    # invalids = StringField('Есть ли инвалиды')
    children = RadioField('Есть ли дети', choices=['Да', 'Нет'])
    children_age = StringField('Возраст детей')
    food = RadioField('Нужна ли еда?', choices=['Да', 'Нет'])
    diet = StringField('Особенности диеты?')
    water = RadioField('Нужна ли вода?', choices=['Да', 'Нет'])
    drugs = RadioField('Нужны ли лекарства?', choices=['Да', 'Нет'])
    drugs_detail = StringField('Укажите какие')
    gigien = RadioField('Нужны ли средства гигиены?', choices=['Да', 'Нет'])
    gigien_detail = StringField('Укажите какие')
    pampers = RadioField('Нужны ли памперсы?', choices=['Да', 'Нет'])
    pampers_detail = StringField('Укажите какие')
    pers_data_agreement = RadioField('Даю согласие на обработку персональных данных', choices=['Да', 'Нет'])
    photo_agreement = RadioField('Даю согласие на фото/видео.', choices=['Да', 'Нет'])