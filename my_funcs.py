from view import mydb
def write_to_base(citizenDataToDb):
    mycol = mydb["people"]
    try:
        mycol.insert_one(citizenDataToDb)
    except:
        pass