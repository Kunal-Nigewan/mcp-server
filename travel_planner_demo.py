
import json
import time


def search_flights():
    time.sleep(0.2)
    return {
        "status": "success",
        "simulated": True,
        "origin": "Bengaluru",
        "destination": "Goa",
        "flights": [
            {
                "airline": "Sample Airways",
                "flight": "SA-201",
                "departure": "08:00",
                "arrival": "09:15",
                "price_inr": 3500,
            },
            {
                "airline": "Demo Air",
                "flight": "DA-105",
                "departure": "11:30",
                "arrival": "12:45",
                "price_inr": 4200,
            },
        ],
    }


def search_hotels():
    time.sleep(0.2)
    return {
        "status": "success",
        "simulated": True,
        "destination": "Goa",
        "hotels": [
            {
                "name": "Example Beach Hotel",
                "rating": 4.2,
                "price_per_night_inr": 2500,
            },
            {
                "name": "Demo Palm Resort",
                "rating": 4.5,
                "price_per_night_inr": 3800,
            },
        ],
    }


def check_weather():
    time.sleep(0.2)
    return {
        "status": "success",
        "simulated": True,
        "destination": "Goa",
        "forecast": {
            "condition": "Partly cloudy",
            "temperature_celsius": 29,
            "suggestion": "Carry sunscreen and stay hydrated.",
        },
    }


def generate_itinerary():
    time.sleep(0.2)
    return {
        "status": "success",
        "simulated": True,
        "duration_days": 3,
        "itinerary": [
            {
                "day": 1,
                "activities": [
                    "Arrive in Goa",
                    "Check in to hotel",
                    "Visit a nearby beach",
                ],
            },
            {
                "day": 2,
                "activities": [
                    "Explore local attractions",
                    "Enjoy a beach afternoon",
                    "Try local cuisine",
                ],
            },
            {
                "day": 3,
                "activities": [
                    "Visit a local market",
                    "Check out of hotel",
                    "Return to Bengaluru",
                ],
            },
        ],
    }


def main():
    print("Starting AI Travel Planner workflow...")

    results = {
        "request": "Plan a 3-day trip to Goa from Bengaluru",
        "notice": (
            "Demonstration only: all travel, hotel, and weather "
            "data is simulated. No bookings are made."
        ),
        "steps": [
            {"name": "flight_search", "result": search_flights()},
            {"name": "hotel_search", "result": search_hotels()},
            {"name": "weather_check", "result": check_weather()},
            {"name": "itinerary_generation", "result": generate_itinerary()},
        ],
    }

    print(json.dumps(results, indent=2))
    print("Travel Planner workflow completed successfully.")


if __name__ == "__main__":
    main()
