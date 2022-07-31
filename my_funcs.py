# from view import mydb
# def write_to_base(citizenDataToDb):
#     mycol = mydb["people"]
#     try:
#         mycol.insert_one(citizenDataToDb)
#     except:
#         pass
# from flask_admin import A
def log(text):
    with open ('log.txt', 'a') as f:
        f.write(text)