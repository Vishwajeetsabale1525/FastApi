from fetch_random_users import fetch_random_users
import asyncio
from fetch_weather_async import main as fetch_weather_main

if __name__ == "__main__":
    print("=== Fetch Random Users ===")
    fetch_random_users(count=5)

    print("\n=== Fetch Weather Data Asynchronously ===")
    asyncio.run(fetch_weather_main())
