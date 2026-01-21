from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "HYD"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=180)

for destination in sheet_data:
    print(f"Checking flights for {destination['city']}...")

    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        tomorrow,
        six_months_from_today,
    )

    cheapest_flight = find_cheapest_flight(flights)

    print(
        f"{destination['city']} | "
        f"Sheet Price: ₹{destination['lowestPrice']} | "
        f"Found: ₹{cheapest_flight.price}"
    )

    if (
        cheapest_flight.price != "N/A"
        and cheapest_flight.price < destination["lowestPrice"]
    ):
        message = (
            f"✈️ Low price alert!\n\n"
            f"Only ₹{cheapest_flight.price} to fly from "
            f"{cheapest_flight.origin_airport} to "
            f"{cheapest_flight.destination_airport}.\n"
            f"Departure: {cheapest_flight.out_date}\n"
            f"Return: {cheapest_flight.return_date}"
        )

        notification_manager.send_whatsapp(message)
