from wtforms import Form,  StringField, TextAreaField

citizen_data = {'fio': '', 'phone': '', 'birth': '', 'addr': '', 'people_num': '', 'people_fio': '',
                             'invalids': '', 'children': '', 'children_age': '', 'food': '', 'drugs': '', 'water': '',
                             'products_detail': '', 'gigien': '', 'gigien_num': '', 'pampers': '', 'diet': '',
                             'pers_data_agreement': '', 'photo_agreement': ''}


class CitizenForm(Form):
    # fio = StringField('ФИО')
    family = StringField('Фамилия')
    name = StringField('Имя')
    paternal = StringField('Отчество')
    phone = StringField('Телефон')
    birth = StringField('Дата рождения')
    # addr = StringField('Адресс')
    city = StringField('Город')
    distr = StringField('Район')
    street = StringField('Улица')
    house = StringField('Дом')
    apartment = StringField('Квартира')
    people_num = StringField('Число проживающих')
    people_fio = StringField('Фио проживающих')
    invalids = StringField('Есть ли инвалиды')
    children = StringField('Есть ли дети')
    children_age = StringField('Возраст детей')
    food = StringField('Нужна ли еда?')
    diet = StringField('Особенности диеты?')
    water = StringField('Нужна ли вода?')
    drugs = StringField('Нужны ли лекарства?')
    drugs_detail = StringField('Укажите какие')
    gigien = StringField('Средства гигиены?')
    gigien_detail = StringField('Укажите какие')
    pampers = StringField('Памперсы?')
    pampers_detail = StringField('Укажите какие')
    pers_data_agreement = StringField('Даю согласие на обработку персональных данных')
    photo_agreement = StringField('Даю согласие на фото/видео.')