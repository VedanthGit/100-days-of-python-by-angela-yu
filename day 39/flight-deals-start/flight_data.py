class FlightData:
    """Holds structured flight information."""

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(data):
    if data is None or not data.get("data"):
        print("No Flight Data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = data["data"][0]
    lowest_price = float(first_flight["price"]["grandTotal"])

    cheapest_flight = FlightData(
        lowest_price,
        first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"],
        first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"],
        first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0],
        first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0],
    )

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < cheapest_flight.price:
            cheapest_flight = FlightData(
                price,
                flight["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"],
                flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0],
                flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0],
            )

    return cheapest_flight
