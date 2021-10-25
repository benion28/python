import phonenumbers
from number_test import number

# Country History
from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

# Service Carrier
from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))