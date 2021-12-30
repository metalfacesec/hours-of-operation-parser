import os
import csv
from model.Restaurant import Restaurant
from utils.HoursUtils import HoursUtils

class RestaurantUtils:
    @staticmethod
    def get_all():
        restaurants = []

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/../data/restaurants.csv', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            next(csv_reader)
            for row in csv_reader:
                restaurants.append(Restaurant(row[0], row[1]))

        return restaurants

    @staticmethod
    def get_open_restaurants(restaurants, day_of_week, time_stamp):
        open_resturaunts = []

        for restaurant in restaurants:
            if HoursUtils.is_restaurant_open(restaurant.get_daily_hours(), day_of_week, time_stamp):
                open_resturaunts.append(restaurant.get_name())

        return open_resturaunts
