import phonenumbers
from number_test import number

# Country History
from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
carrier_country = geocoder.description_for_number(ch_number, "en")
print(f"Carrier Country: { carrier_country }")

# Service Carrier
from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
carrier_name = carrier.name_for_number(service_number, "en")
print(f"Carrier Name: { carrier_name }")