import unittest

from utils.RestaurantUtils import RestaurantUtils

class TestRestaurantUtilsMethods(unittest.TestCase):
    def test_get_open_restaurants(self):
        restaurants = RestaurantUtils.get_all()

        correct = [
            "The Cowfish Sushi Burger Bar",
            "Morgan St Food Hall",
            "Garland",
            "Crawford and Son",
            "Caffe Luna",
            "Bida Manda",
            "The Cheesecake Factory",
            "Tupelo Honey",
            "Player's Retreat",
            "Glenwood Grill",
            "Neomonde",
            "Page Road Grill",
            "Mez Mexican",
            "Saltbox",
            "El Rodeo",
            "Provence",
            "Tazza Kitchen",
            "Mandolin",
            "Mami Nora's",
            "Gravy",
            "Taverna Agora",
            "Char Grill",
            "Seoul 116",
            "Whiskey Kitchen",
            "Sitti",
            "Stanbury",
            "Yard House",
            "David's Dumpling",
            "Gringo a Gogo",
            "Brewery Bhavana",
            "Dashi",
            "42nd Street Oyster Bar",
            "Top of the Hill",
            "Jose and Sons",
            "Oakleaf",
            "Second Empire"
        ]
        self.assertEqual(RestaurantUtils.get_open_restaurants(restaurants, "tue", "13:00"), correct)

        correct = [ "Seoul 116" ]
        self.assertEqual(RestaurantUtils.get_open_restaurants(restaurants, "sun", "02:00"), correct)

        correct = ["Seoul 116", "42nd Street Oyster Bar"]
        self.assertEqual(RestaurantUtils.get_open_restaurants(restaurants, "mon", "02:00"), correct)

        correct = [
            "Caffe Luna",
            "Bonchon",
            "Seoul 116",
            "Stanbury",
            "42nd Street Oyster Bar"
        ]
        self.assertEqual(RestaurantUtils.get_open_restaurants(restaurants, "tue", "00:00"), correct)

if __name__ == '__main__':
    unittest.main()
