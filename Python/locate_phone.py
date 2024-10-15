from phonenumbers import geocoder
import phonenumbers

number = phonenumbers.parse("+917703868519", "IN")

print(geocoder.description_for_number(number, "en"))
