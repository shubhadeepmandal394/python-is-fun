import phonenumbers
from test import number

# mobile phone number
details = phonenumbers.parse(number, None)
print("\nPhone Number: ", number)
print(details)

# location
from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
print("Location: ", end='')
print(geocoder.description_for_number(ch_number, "en"))

# carrier
from phonenumbers import carrier
ro_number = phonenumbers.parse(number, "RO")
print("Carrier(originally owned): ", end='')
print(carrier.name_for_number(ro_number, "en"))

# timezone
#from phonenumbers import timezone
#gb_number = phonenumbers.parse(number, "GB")
#print("timezone: ", end='')
#print(timezone.time_zones_for_number(gb_number, "en"))
