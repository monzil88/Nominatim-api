# packages
import time
import requests
import json


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


    def address_list(self, input_file):

        addresses = ''
        # fetch from a file
        with open(input_file, 'r') as f:
            for line in f.read():
                addresses += line
        print(addresses)
        # convert addresses into list
        addresses = addresses.split('\n')
        print(addresses)

        return addresses

    def parse(self, response_in_json):
        print(json.dumps(response_in_json, indent=2))

    def run(self, input_file):
        # collect the address from the input fil
        addresses = self.address_list(input_file)
        for address in addresses:
            res = self.fetch(address).json()
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
    geocoder.run(input_file=input("Type filename\n"))
