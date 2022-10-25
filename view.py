from app import app
import datetime
# 20.20, 20/10
from time import time, asctime
from bson.objectid import ObjectId
import re
from flask import render_template, request, redirect, url_for
from flask import send_file
# import pymongo
from forms import CitizenForm
from datetime import datetime
from app import mydb
from models import Cit
table_name = "people_new17_08"
from my_funcs import log
import csv
count = 0
citizen_data = {'fio': {'family': '', 'name': '', 'paternal': ''}, 'phone': '', 'birth': '', 'addr': {'city': '',
                             'distr': '', 'street': '', 'house': '', 'apartment': ''}, 'people_num': '',
                             'people_fio': '', 'invalids': '', 'children': '', 'children_age': '', 'food': '',
                             'diet': '', 'water': '', 'drugs': '', 'drugs_detail': '', 'gigien': '', 'gigien_detail': '',
                             'pampers': '', 'pampers_detail': '', 'pers_data_agreement': '', 'photo_agreement': ''}
citizen_data_list = ['fio', 'phone', 'birth', 'addr', 'people_num', 'people_fio', 'invalids', 'children',
                     'children_age', 'food', 'diet', 'water', 'drugs', 'drugs_detail', 'gigien', 'gigien_detail', 'pampers',
                     'pampers_detail', 'pers_data_agreement', 'photo_agreement', 'birth_year','_id']



def write_to_base(citizenDataToDb):
    mycol = mydb[table_name]
    try:
        pers = mycol.insert_one(citizenDataToDb)
        # pers.inserted_id
        # with open('log.txt', 'a') as f:
        #     f.write(str(pers.inserted_id))
        return pers.inserted_id
    except:
        pass

def write_to_csv(citizenDataToCSV):
    citizen_info = ['fio', 'phone', 'birth', 'addr', 'people_num', 'people_fio',
                    'invalids', 'children', 'children_age', 'food', 'drugs', 'water',
                    'products_detail', 'gigien', 'gigien_num', 'pampers', 'diet',
                    'pers_data_agreement', 'photo_agreement', 'birth_year', '_id']
    with open('citizens.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=citizen_data_list)
        writer.writeheader()
        writer.writerows(citizenDataToCSV)

@app.route('/create', methods=['POST', 'GET'])
def citizen_create():
    if request.method == 'POST':
        #get FIO
        family = request.form['family']
        name = request.form['name']
        paternal = request.form['paternal']
        fio = {'family': family, 'name': name, 'paternal': paternal}
        #end get FIO
        citizen_data['fio'] = fio
        citizen_data['phone'] = request.form['phone']
        citizen_data['birth'] = request.form['birth']

        log(str(citizen_data['birth']))
        # birth_date = datetime.strptime(citizen_data['birth'], '%Y-%m-%d')
        birth_date = datetime.strptime(citizen_data['birth'], '%d.%m.%Y')
        bith_year = birth_date.year
        citizen_data['birth_year'] = bith_year
        #get ADDR
        city = request.form['city']
        distr = request.form['distr']
        street = request.form['street']
        house = request.form['house']
        apartment = request.form['apartment']
        addr = {'city': city, 'distr': distr, 'street': street, 'house': house, 'apartment': apartment}
        citizen_data['addr'] = addr
        #end get ADDR
        citizen_data['people_num'] = request.form['people_num']
        citizen_data['people_fio'] = request.form['people_fio']
        citizen_data['invalids'] = request.form['invalids']
        citizen_data['children'] = request.form['children']
        citizen_data['children_age'] = request.form['children_age']
        citizen_data['food'] = request.form['food']
        citizen_data['diet'] = request.form['diet']
        citizen_data['water'] = request.form['water']
        citizen_data['drugs'] = request.form['drugs']
        citizen_data['drugs_detail'] = request.form['drugs_detail']
        citizen_data['gigien'] = request.form['gigien']
        citizen_data['gigien_detail'] = request.form['gigien_detail']
        citizen_data['pampers'] = request.form['pampers']
        citizen_data['pampers_detail'] = request.form['pampers_detail']
        citizen_data['pers_data_agreement'] = request.form['pers_data_agreement']
        citizen_data['photo_agreement'] = request.form['photo_agreement']



        # 'fio': '', 'phone': '', 'birth': '', 'addr': '', 'people_num': '', 'people_fio': '',
        #                 'invalids': '', 'children': '', 'children_age': '', 'food': '', 'drugs': '', 'water': '',
        #                 'products_detail': '', 'gigien': '', 'gigien_num': '', 'pampers': '', 'diet': '',
        #                 'pers_data_agreement': '', 'photo_agreement': ''}
        # with open('log.txt', 'a') as f:
        #     f.write(f'{citizen_data}' + '\n')
        # try:
        #     pass
        write_to_base(citizen_data)
        write_to_csv([citizen_data])
        return redirect(url_for('showall'))

    form = CitizenForm()
    return render_template('citizen_create.html', form=form)
@app.route('/download_file')
def download_file():
    log('line111')
    mycol = mydb[table_name]
    cits = mycol.find()
    cits_list = []
    for cit in cits:
        cits_list.append(cit)
    #     print(str(x))
    actual_time = str(datetime.now())
    download_path = f"citizensdata{actual_time}.csv"
    # log(str(cits_list))
    # for c in cits_list:
    #     log(str(c)+'\n')
    with open(download_path, 'w') as file:
        log(str(cits_list))
        writer = csv.DictWriter(file, fieldnames=citizen_data_list)
        writer.writeheader()
        writer.writerows(cits_list)

    return send_file(download_path, as_attachment=True)#on server
    # return send_file('templates/' + download_path, as_attachment=True) # local

@app.route('/street_search')
def street_search():
    q = request.args.get('q')
    text_to_send = []
    if q:
        street = q
        cits = mydb.people_new17_08
        cits_with_street = cits.find({'addr.street': re.compile('^' + re.escape(street) + '$', re.IGNORECASE)})
        cit_list = list(cits_with_street)

        # if len(cit_list) > 0:

            # for cit in cit_list:
            #     text_to_send.append(cit)
        # else:
        #     return 'Нет людей с этой улицы'

        for cit in cit_list:
            text_to_send.append(cit)
    return render_template('street_search.html', pers_info=text_to_send)


@app.route('/name_search')
def name_search():
    global count
    q = request.args.get('q')
    text_to_send = ''
    # log(str(q))
    # log('line138')
    if q:
        count += 1
        person = q
        cits = mydb.people_new17_08
        cits_with_name = cits.find({'fio.family': re.compile('^' + re.escape(person) + '$', re.IGNORECASE)})
        cit_list = list(cits_with_name)
        # log(str(count))
        # log(str(len(cit_list) + 1))
        # for el in cit_list:
        #     log(str(el))
        #     log('\n')


        if cit_list:
            text_to_send = []
            for cit in cit_list:
                text_to_send.append(cit)
                # text_to_send.append('Фамилия: ' + cit['fio']['family'])
            # text_to_send = f"1. Фамилия: {cit['fio']['family']}, \n"\
            #                f"2. Телефон: {cit['phone']}\n"
                           # f"3. Датa рождения: {cit['birth']}\n" \
                           # f"4. Адрес: {cit['addr']}\n" \
                           # f"5. Число проживающих: {cit['people_num']}\n" \
                           # f"6. ФИО и возраст проживающих: {cit['people_fio']}\n" \
                           # f"7. Есть ли среди проживающих инвалиды? {cit['invalids']}\n" \
                           # f"8. Наличие детей: {cit['children']}\n" \
                           # f"9. Возраст детей: {cit['children_age']}\n" \
                           # f"10. Небходимость продуктов питания: {cit['food']}\n" \
                           # f"11. Воды: {cit['water']}\n" \
                           # f"12. Лекарств: {cit['drugs']}\n" \
                           # f"13. Kоличество: {cit['products_detail']}\n" \
                           # f"14. Средства личной гигиены: {cit['gigien']}\n" \
                           # f"15. Kоличество {cit['gigien_num']}\n" \
                           # f"16. Памперсы: {cit['pampers']}\n" \
                           # f"17. Особенности диеты и т.п.: {cit['diet']}\n" \
                           # f"18. Cогласие на обработку персональных данных: {cit['pers_data_agreement']} \n" \
                           # f"19. Cогласие на фото/видео: {cit['photo_agreement']}\n"
        else:
            text_to_send = 'Нет человека с такой фамилией!'
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
            mycol = mydb[table_name]
            # mycol = mydb["people"]
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

@app.route('/<id_>/delete/', methods=['POST', 'GET'])
def citizen_delete(id_):
    cits = mydb.people_new17_08
    cits.delete_one({'_id': ObjectId(id_)})
    return redirect(url_for('showall'))



@app.route('/<id_>/edit/', methods=['POST', 'GET'])
def citizen_edit(id_):
    cits = mydb.people_new17_08
    cit_ = cits.find_one({'_id': ObjectId(id_)})
    cit = Cit(cit_['fio']['family'], cit_['phone'], cit_['birth'], cit_['people_fio'])
    if request.method == 'POST':
        # log('194')
        # form = CitizenForm(obj=cit)
        form = CitizenForm(formdata=request.form, obj=cit)
        #get data from form
        # get fio
        family = request.form['family']
        if not family:
            family = cit_['fio']['family']
        name = request.form['name']
        paternal = request.form['paternal']
        #get phone
        phone = request.form['phone']
        #get birth
        birth = request.form['birth']
        # get adress
        city = request.form['city']
        distr = request.form['distr']
        street = request.form['street']
        house = request.form['house']
        apartment = request.form['apartment']
        people_fio = request.form['people_fio']
        #change values
        myquery = cits.find_one({'_id': ObjectId(id_)})
        newvalues = {"$set": {"fio.family": family, "fio.name": name, "fio.paternal": paternal, "phone": phone, "birth": birth, "addr.city": city, "addr.distr": distr, "addr.street": street, "addr.house": house, "addr.apartment": apartment, "people_fio": people_fio}}
        # log('line 200\n')
        # log(str(myquery))
        cits.update_one(myquery, newvalues)
        # cit.fio = request.form['family']
        # cit.phone = request.form['phone']
        # cit.birth = request.form['birth']
        # birth_date = datetime.strptime(cit_['birth'], '%d.%m.%Y')
        # bith_year = birth_date.year
        # cit.birth_year = bith_year
        # citizen_data['fio']['family'] = request.form['family']
        # citizen_data['phone'] = request.form['phone']
        # citizen_data['birth'] = request.form['birth']
        # birth_date = datetime.strptime(citizen_data['birth'], '%d.%m.%Y')
        # # bith_year = birth_date.year
        # citizen_data['birth_year'] = bith_year
        #
        # # with open('log.txt', 'a') as f:
        # #     f.write(str(cit.fio))
        # # log(str(citizen_data))
        # # log(str(write_to_base(citizen_data)) + 'line213')
        # new_id = write_to_base(citizen_data)
        # new_cit = cits.find_one({'_id': ObjectId(new_id)})
        # log(str(new_id) + ' line216')
        # form.populate_obj(cit)
        # # result = cits.delete_one({'_id': ObjectId(id_)})
        # return redirect(url_for('citizen_edit', id_=new_cit['_id']))

        return redirect(url_for('showall'))
    form = CitizenForm(obj=cit)
    # return redirect(url_for('showall'))
    return render_template('citizen_edit.html', id_=id_, form=form)


@app.route('/<id>')
def cit_detail(id):
    cits = mydb.people_new17_08
    # cits = mydb.people
    cit = cits.find_one({'_id': ObjectId(id)})

    # with open('log.txt', 'a') as f:
    #     f.write(id)

    text_to_send = [f"1. ФИО: {cit['fio']['family']} {cit['fio']['name']} {cit['fio']['paternal']}\n",
                   f"2. Телефон: {cit['phone']}\n",
                   f"3. Датa рождения: {cit['birth']}\n",
                   f"4. Адрес: город: {cit['addr']['city']}, район: {cit['addr']['distr']}, улица: {cit['addr']['street']}, дом: {cit['addr']['house']}, квартира: {cit['addr']['apartment']}\n",
                   f"5. Число проживающих: {cit['people_num']}\n",
                   f"6. ФИО и возраст проживающих: {cit['people_fio']}\n",
                   f"7. Есть ли среди проживающих инвалиды? {cit['invalids']}\n",
                   f"8. Наличие детей: {cit['children']}\n",
                   f"9. Возраст детей: {cit['children_age']}\n",
                   f"10. Небходимость продуктов питания: {cit['food']}\n",
                   f"11. Воды: {cit['water']}\n",
                   f"12. Лекарств: {cit['drugs']}\n",
                   f"14. Средства личной гигиены: {cit['gigien']}\n",
                   f"15. Kоличество {cit['gigien_detail']}\n",
                   f"16. Памперсы: {cit['pampers']}\n",
                   f"17. Особенности диеты: {cit['diet']}\n",
                   f"18. Cогласие на обработку персональных данных: {cit['pers_data_agreement']} \n",
                   f"19. Cогласие на фото/видео: {cit['photo_agreement']}\n"]
    # log(str(cit))
    _id = ObjectId(cit['_id'])
    return render_template('cit_detail.html', pers_info=text_to_send, _id=_id)

    pass


@app.route('/showall')
def showall():
    global count
    # log('SowAll')
    count += 1
    mycol = mydb[table_name]
    # mycol = mydb["people"]
    # log('Full unformation row 149')
    cit = []
    text_to_send = ''
    row_num = 1
    for x in mycol.find():
        pers = f"Фамилия: {x['fio']['family']} , Имя: {x['fio']['name']}, Отчество: {x['fio']['paternal']}, дата рождения: {x['birth']}"
        cit.append(pers)
    #
    log(str(count))
    return render_template('showall.html', cit=mycol.find())
    # return render_template('showall.html', cit=cit)
