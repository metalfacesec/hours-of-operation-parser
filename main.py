import urllib
from dateutil import parser
from utils.RestaurantUtils import RestaurantUtils
from utils.HttpResponseUtils import HttpResponseUtils
from http.server import BaseHTTPRequestHandler, HTTPServer

all_restaurants = None

if __name__ == '__main__':
    all_restaurants = RestaurantUtils.get_all()

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if all_restaurants is None:
            message = "Unable to process you're request, no restaurants found or restaurants not done processing"
            return HttpResponseUtils.get_bad_request_response(self, message)

        params = urllib.parse.parse_qs(self.path[2:])
        if 'date' not in params:
            message = "Unable to process you're request, no restaurants found or restaurants not done processing"
            return HttpResponseUtils.get_bad_request_response(self, message)

        day_of_week = parser.parse(params['date'][0]).strftime("%a").lower()  # Day of week
        time = parser.parse(params['date'][0]).strftime("%H:%M")  # time 24 hour

        # TODO: Validate the day and time
        
        data = RestaurantUtils.get_open_restaurants(all_restaurants, day_of_week, time)
        HttpResponseUtils.get_success_response(self, 'success', data)

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()

