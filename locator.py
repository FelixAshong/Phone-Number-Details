from scripts.banner import banner2, banner, clear
from scripts.colors import ran, y, c, g, lg, r
import sys
import os
import requests

try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    os.system("pip install colorama")

from phonenumbers import carrier, geocoder, timezone, NumberParseException

try:
    import phonenumbers
except ModuleNotFoundError:
    os.system("pip install phonenumbers")

try:
    import fontstyle
except ModuleNotFoundError:
    os.system("pip install fontstyle")

# Define your numverify API key
NUMVERIFY_API_KEY = "your_actual_api_key_here"

clear()
banner()


def exit():
    sys.exit()


def get_additional_info_from_api(mobile_number):
    try:
        response = requests.get(f"https://apilayer.com/numverify/validate?access_key={NUMVERIFY_API_KEY}&number={mobile_number}")
        data = response.json()

        if data['valid']:
            return data['carrier'], data['location']
        else:
            return None, None
    except Exception as e:
        print(ran, "Error fetching additional information from the API:", e)
        return None, None


def program():
    try:
        mobile_number = input(ran + "\nType phone number with country code: " + Style.BRIGHT + Fore.LIGHTYELLOW_EX)
        mobile_number = mobile_number.replace(" ", "")
        try:
            mobile_number = phonenumbers.parse(mobile_number)
        except NumberParseException:
            print(r, "Wrong Input format")
            exit()

        print(c, "\nTime Zone for entered number: ")
        print(c, timezone.time_zones_for_number(mobile_number))
        print(y, "\nCarrier name: ")
        print(y, carrier.name_for_number(mobile_number, "en"))
        print(g, "\nGeocoder Discripton: ")
        print(g, geocoder.description_for_number(mobile_number, "en"))
        print(r, "\nValid phone number: ")
        if phonenumbers.is_valid_number(mobile_number) == True:
            print(r, "Yeah, the phonenumber is valid ")
        else:
            print(r, "No, the number is not valid ")

        print(y, "\nChecking possible number: ")
        print(y, phonenumbers.is_possible_number(mobile_number))

        # Additional information based on user input
        cont_additional_info = input(ran + "\nDo you want to fetch additional information (carrier and location) from the API? [y/n]: " + lg).lower()

        if cont_additional_info in yes:
            carrier_info, location_info = get_additional_info_from_api(mobile_number)

            if carrier_info and location_info:
                print(y, "\nAdditional Information (from API):")
                print(y, f"Carrier: {carrier_info}")
                print(y, f"Location: {location_info}")
            else:
                print(r, "Failed to fetch additional information from the API.")

    except ValueError:
        print(ran, "\nHey! What are doing man!")
    except KeyboardInterrupt:
        print(ran, "\nHave a good day dear :-) ")


no = ["no", "n"]

yes = ["yes", "y"]
cont = ""

while cont not in no:
    program()

    cont = input(ran + "\nDo you want to continue? [y/n]:" + lg).lower()

    if cont in yes:
        os.system("cls" if os.name == 'nt' else 'clear')
        banner()
    elif cont in no:
        banner2()
