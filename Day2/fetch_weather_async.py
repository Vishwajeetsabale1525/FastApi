import asyncio
import httpx
import csv
import os
from datetime import datetime

# Replace with your own OpenWeatherMap API key
API_KEY = "a8ca0661cf3058a1e06c33a57dcab665"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# List of cities
cities = ["London", "New York", "Tokyo", "Sydney", "Mumbai"]

async def fetch_weather(client, city):
    """
    Fetch weather data for a single city asynchronously.
    """
    try:
        response = await client.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
        response.raise_for_status()
        data = response.json()
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"]
        }
    except httpx.HTTPStatusError as e:
        print(f"HTTP error for {city}: {e}")
        return {"city": city, "temperature": None, "weather": None}
    except Exception as e:
        print(f"Error fetching {city}: {e}")
        return {"city": city, "temperature": None, "weather": None}

async def main():
    """
    Fetch weather for multiple cities concurrently and save results to CSV.
    """
    # Ensure the results folder exists
    os.makedirs("results", exist_ok=True)

    async with httpx.AsyncClient() as client:
        tasks = [fetch_weather(client, city) for city in cities]
        results = await asyncio.gather(*tasks)
    
    # Save results to CSV
    filename = f"results/weather_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["city", "temperature", "weather"])
        writer.writeheader()
        writer.writerows(results)
    
    print(f"Weather data saved to {filename}")

if __name__ == "__main__":
    asyncio.run(main())
