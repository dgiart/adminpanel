from wtforms import Form,  StringField, TextAreaField

citizen_data = {'fio': '', 'phone': '', 'birth': '', 'addr': '', 'people_num': '', 'people_fio': '',
                             'invalids': '', 'children': '', 'children_age': '', 'food': '', 'drugs': '', 'water': '',
                             'products_detail': '', 'gigien': '', 'gigien_num': '', 'pampers': '', 'diet': '',
                             'pers_data_agreement': '', 'photo_agreement': ''}

class CitizenForm(Form):
    fio = StringField('ФИО')
    phone = StringField('Телефон')
    birth = StringField('Дата рождения')
    addr = StringField('Адресс')
    people_num = StringField('Число проживающих')
    people_fio = StringField('Фио проживающих')
    invalids = StringField('Есть ли инвалиды')
    children = StringField('Есть ли дети')
    children_age = StringField('Возраст детей')
    food = StringField('Нужна ли еда?')
    drugs = StringField('Нужны ли лекарства?')
    water = StringField('Нужна ли вода?')
    products_detail = StringField('Какие продукты?')
    gigien = StringField('Средства гигиены?')
    gigien_num = StringField('Какое количество?')
    diet = StringField('Особенности диеты?')
    pers_data_agreement = StringField('Даю согласие на обработку персональных данных')
    photo_agreement = StringField('Даю согласие на фото/видео.')