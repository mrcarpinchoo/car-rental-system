#!/usr/bin/env python3

# third-party libraries
import ply.yacc as yacc

# custom modules
from lex import tokens

def p_cars(p):
    "cars : CARS_O car_list CARS_C"

    values = p[2].rstrip(',\n') + '\n;'

    p[0] = f"INSERT INTO cars (id, brand, model, year, license_plate, available, rental_price, transmission, services)\nVALUES\n{values}"
# end def

def p_car_list(p):
    "car_list : car car_list"

    p[0] = p[1] + p[2]
# end def

def p_car_list_empty(p):
    "car_list : "

    p[0] = ""
# end def

def p_car(p):
    "car : CAR_O id brand model year license_plate available rental_price transmission services CAR_C"

    p[0] = f"\t('{p[2]}', '{p[3]}', '{p[4]}', '{p[5]}', '{p[6]}', '{p[7]}', '{p[8]}', '{p[9]}', '{p[10]}'),\n"
# end def

def p_id(p):
    "id : ID_O ID ID_C"

    p[0] = p[2]
# end def

def p_brand(p):
    "brand : BRAND_O TEXT BRAND_C"

    p[0] = p[2]
# end def

def p_model(p):
    "model : MODEL_O TEXT MODEL_C"

    p[0] = p[2]
# end def

def p_year(p):
    "year : YEAR_O YEAR YEAR_C"

    p[0] = p[2]
# end def

def p_license_plate(p):
    "license_plate : LICENSE_PLATE_O LICENSE_PLATE LICENSE_PLATE_C"

    p[0] = p[2]
# end def

def p_available(p):
    "available : AVAILABLE_O AVAILABLE AVAILABLE_C"

    p[0] = p[2]
# end def

def p_rental_price(p):
    "rental_price : RENTAL_PRICE_O RENTAL_PRICE RENTAL_PRICE_C"

    p[0] = p[2]
# end def

def p_transmission(p):
    "transmission : TRANSMISSION_O TRANSMISSION TRANSMISSION_C"

    p[0] = p[2]
# end def

def p_services(p):
    "services : SERVICES_O service_list SERVICES_C"

    p[0] = p[2]
# end def

def p_service_list(p):
    "service_list : service service_list"

    if p[2]: p[0] = f"{p[1]}, {p[2]}"
    else: p[0] = p[1]
        
    # p[0] = f"{p[1]}, {p[2]}"
# end def

def p_service_list_empty(p):
    "service_list : "

    p[0] = ""
# end def

def p_service(p):
    "service : SERVICE_O date description SERVICE_C"

    p[0] = f"\"{p[2]}\": \"{p[3]}\""
# end def

def p_date(p):
    "date : DATE_O DATE DATE_C"

    p[0] = p[2]
# end def

def p_description(p):
    "description : DESCRIPTION_O TEXT DESCRIPTION_C"

    p[0] = p[2]
# end def

# error rule for syntax errors
def p_error(p):
    print(f"Syntax error in input: {p}")
# end def

parser = yacc.yacc()

clean_source = ""

with open("data/cars.xml", "r", encoding="utf-8") as file:
    for line in file: clean_source += line.strip()
    # end for-in

    result = parser.parse(clean_source)

    print(f"Result:\n{result}")
# end with