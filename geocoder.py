# packages
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

    def parse(self, res_in_json):
        print(json.dumps(res_in_json, indent=2))

    def run(self, input_address):
        # WE need the response in json format
        res_in_json = self.fetch(input_address).json()
        # print(res_in_json)
        self.parse(res_in_json)


# main driver
if __name__ == '__main__':
    geocoder = Geocoder()
    geocoder.run(input_address=input("Type address\n"))
