# packages
import time
import requests
import json


def address_list(input_file):

    addresses = ''
    # fetch from a file
    with open(input_file, 'r') as f:
        for line in f.read():
            addresses += line
    # print(addresses)
    # convert addresses into list
    addresses = addresses.split('\n')

    # print(addresses)

    return addresses


class Geocoder:
    # base URL
    base_url = 'https://nominatim.openstreetmap.org/search'

    def fetch(self, address):
        # String query parameters
        params = {'q': address,
                  'format': 'geojson',
                  }
        coded_response = requests.get(url=self.base_url, params=params)
        print("\nHTTP GET request to URL: \n" + str(coded_response.url)
              + " \n Status Code : " + str(coded_response.status_code))

        if coded_response.status_code == 200:
            return coded_response
        else:
            return None

    def parse(self, response_in_json):
        try:
            display_address = json.dumps(response_in_json["features"][0]["properties"]["display_name"], indent=2).replace('\"', '')
            coordinates = json.dumps(response_in_json["features"][0]["geometry"]["coordinates"], indent=2)\
                .replace('\n', '').replace('[', '').replace(']', '').replace('  ', '').replace(',', ', ')

            items = {
                'Address': display_address,
                'Coordinates': coordinates,
            }
            print(json.dumps(items, indent=2))

        except:
            pass

    def run(self, input_file):
        # collect the address from the input file
        addresses = address_list(input_file)
        for address in addresses:

            # collect response in json format
            res = self.fetch(address).json()
            # print(address)
            self.parse(response_in_json=res)

            # adhere nominatim policy
            time.sleep(2)

    # Single Address search
        # WE need the response in json format
        # res_in_json = self.fetch(input_address).json()
        # print(res_in_json)
        # self.parse(res_in_json)


# main driver
if __name__ == '__main__':
    geocoder = Geocoder()
    geocoder.run(input_file="address.txt")
