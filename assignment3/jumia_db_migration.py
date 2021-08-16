import pymysql
from jumia_all_pages import *

connection = pymysql.connect(host= "localhost",
                             user= "root",
                             password= "Ttabitha23",
                             db= "jumia",
                             charset= "utf8mb4",
                             cursorclass= pymysql.cursors.DictCursor)


def create_jumia_tables():
    with connection.cursor() as Cursor:
        create_table_mobile_phones = """
                                CREATE TABLE IF NOT EXISTS mobile_phone(
                                  id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                  phone_brand VARCHAR(60),
                                  old_price INT(10),
                                  new_price INT(10),
                                  rating INT(10)
                                );
        """

        Cursor.execute(create_table_mobile_phones)

        connection.commit()


def write_report_jumia(brand, specification, price_1, price_2, star_rating):
    with connection.cursor() as Cursor:
        add_phones =f"""
                    INSERT INTO mobile_phone(phone_brand, phone_specs, old_price, new_price, rating)
                    VALUES
                    ('{brand}, '{specification}', {price_1} {price_2} '{star_rating}');
        """
        Cursor.execute(add_phones)

        connection.commit

def read_and_send_data():

  extracted_data1 = jumia_data

  for entry in extracted_data1:
    extracted_data = entry
    write_report_jumia(extracted_data[0],
                       extracted_data[1][:10],
                       extracted_data[2],
                       extracted_data[3],
                       str(extracted_data[4])
                       )

