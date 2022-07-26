from app import app
from time import time, asctime
from flask import render_template, request
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["citizens_database"]

@app.route('/name_search')
def name_search():
    q = request.args.get('q')
    text_to_send = ''
    if q:
        person = q
        cits = mydb.people
        cit = cits.find_one({'fio': person})
        text_to_send = f"1. ФИО: {cit['fio']}\n" \
                       f"2. Телефон: {cit['phone']}\n" \
                       f"3. Датa рождения: {cit['birth']}\n" \
                       f"4. Адрес: {cit['addr']}\n" \
                       f"5. Число проживающих: {cit['people_num']}\n" \
                       f"6. ФИО и возраст проживающих: {cit['people_fio']}\n" \
                       f"7. Есть ли среди проживающих инвалиды? {cit['invalids']}\n" \
                       f"8. Наличие детей: {cit['children']}\n" \
                       f"9. Возраст детей: {cit['children_age']}\n" \
                       f"10. Небходимость продуктов питания: {cit['food']}\n" \
                       f"11. Воды: {cit['water']}\n" \
                       f"12. Лекарств: {cit['drugs']}\n" \
                       f"13. Kоличество: {cit['products_detail']}\n" \
                       f"14. Средства личной гигиены: {cit['gigien']}\n" \
                       f"15. Kоличество {cit['gigien_num']}\n" \
                       f"16. Памперсы: {cit['pampers']}\n" \
                       f"17. Особенности диеты и т.п.: {cit['diet']}\n" \
                       f"18. Cогласие на обработку персональных данных: {cit['pers_data_agreement']} \n" \
                       f"19. Cогласие на фото/видео: {cit['photo_agreement']}\n"
    return render_template('name_search.html', pers_info=text_to_send)

@app.route('/birth_search')
def birth_search():
    q = request.args.get('q')
    text_to_send = ''
    if q:
        try:
            years = q.split('-')
            start_year = int(years[0])
            fin_year = int(years[1])
        except:
            text_to_send = 'Неверный формат. Введите интервал лет в формате: \"год1 - год2\"'
            return render_template('birth_search.html')
        if start_year >= fin_year:
            text_to_send = 'Неверный формат. Введите интервал лет в формате: \"год1 - год2\"'
        else:
            # log('line 226')
            mycol = mydb["people"]
            people_in_range = mycol.find({"birth_year": {"$gt": start_year, "$lt": fin_year}})
            # if user_text == 'Информация по конкретному человеку':
            # log(str(people_in_range) + 'line 230')
            text_to_send = ''
            people_list = []
            for x in people_in_range:
                people_list.append(x)
                # print(f"ФИО: {x['fio']}, дата рождения: {x['birth']}")
            for i in range(len(people_list)):
                text_to_send += str(
                    i + 1) + f") ФИО: {people_list[i]['fio']}, дата рождения: {people_list[i]['birth']}\n"
    return render_template('birth_search.html', pers_info=text_to_send)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bot')
def bot():
    return 'hi from bot!!!'
@app.route('/showall')
def showall():
    mycol = mydb["people"]
    # mycol = mydb["people"]
    # log('Full unformation row 149')
    cit = []
    text_to_send = ''
    row_num = 1
    for x in mycol.find():
        pers = f"ФИО: {x['fio']} , дата рождения: {x['birth']}"
        cit.append(pers)
    #

    return render_template('showall.html', cit=cit)