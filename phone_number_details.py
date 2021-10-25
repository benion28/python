import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier


def number_details(value):
    # Country History
    ch_number = phonenumbers.parse(value, "CH")
    country_name = geocoder.description_for_number(ch_number, "en")

    # Service Carrier
    service_number = phonenumbers.parse(value, "RO")
    service_carrier = carrier.name_for_number(service_number, "en")

    print(f"""
Phone Number: { value }
Country Name: { country_name }
Service Carrier: { service_carrier }
    """)


while True:
    number = input("Type In Your Phone Number: ").lower()

    if number == "help" or number == "h":
        print("""
-- help or h -- For Help Menu
-- quit or q -- To Quit Program
        """)
    elif number == "quit" or number == "q":
        break
    else:
        try:
            number_details(number)
        except Exception:
            print("""
-- Error!! Please Try Again --
            """)



