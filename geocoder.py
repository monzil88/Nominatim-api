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
        response = requests.get(url=self.base_url, params=params)
        print("\nHTTP GET request to URL: \n" + str(response.url)
              + " \n Status Code : " + str(response.status_code))

        if response.status_code == 200:
            return response
        else:
            return None

    def parse(self, response):
        pass

    def run(self):
        self.fetch('Beaumont, Pindo Cir')


# main driver
if __name__ == '__main__':
    geocoder = Geocoder()
    geocoder.run()
