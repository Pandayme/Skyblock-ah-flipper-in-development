from asyncore import read
import requests
import json as js
from pprint import pprint

# Functions
def get_info(call):
       r = requests.get(call)
       return r.json()

# Checks auction pages
def auction_data():
    all_auctions = []

    first_page = ("https://api.hypixel.net/skyblock/auctions?page=0")

    auction_data = first_page.get("auctions", [])

    for page in range (1, first_page.get("totalPages", 0) + 1):
        current_page = get_info(f"https://api.hypixel.net/skyblock/auctions?page={page}")
        all_auctions += (current_page.get("auctions", []))

        
        
        return all_auctions


    

# Returns a list of recently ended auctions
def get_recently_ended_auctions():
    return get_info("https://api.hypixel.net/skyblock/auctions_ended")

# Returns a list of active auctions
def get_active_auction_data():
    return get_info("https://api.hypixel.net/skyblock/auctions")





    # Variables

API_File = open("C:/Users/Offic/OneDrive/Desktop/API_KEY.json.", "r")
API_KEY = js.loads(API_File.read())
Item_Filter = {"name" : "Furniture"}





# Code







print (API_KEY)
