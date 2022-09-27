#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager
import flight_search

data_manager = data_manager.DataManager()
flight_search = flight_search.FlightSearch()
#for num in range (0, len(response.json()["prices"])):
    #print(response.json()["prices"][num]["city"])

sheet_data = data_manager.populate_data()
if sheet_data["prices"][0]["iataCode"] == "":
    for num in range (0, len(sheet_data["prices"])):
        #iata_code = flight_search.get_iata((sheet_data["prices"][num]["city"]))
        data_manager.update_code(sheet_data["prices"][num]["id"], sheet_data["prices"][num]["city"])
